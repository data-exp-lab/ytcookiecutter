import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. '
          'Please do not use a - and use _ instead' % module_name)
    sys.exit(1)  # Exit to cancel project

# check that the extra packages required for using this template are installed.
# would be nice if this could happen before the template was generated...
template_reqs = {"yaml": "pyyaml"}
missing_reqs = []
for req, install_name in template_reqs.items():
    try:
        _ = __import__(req)
    except ImportError:
        missing_reqs.append(req)

if missing_reqs:
    print("\nThis template requires some extra modules that are not installed:")
    print( ", ".join(missing_reqs))
    print("Install with:")
    extra_reqs = " ".join(missing_reqs)
    print(f"    pip install {extra_reqs}")
    sys.exit(1)

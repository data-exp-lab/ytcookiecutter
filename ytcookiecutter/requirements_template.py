import os
from typing import Union, List
from .cookiecutter_handler import CookieCutterHandler


def _validate_package_string(package_string):
    has_version = [op in package_string for op in [">=", "==", "<=", "<", ">"]]
    return any(has_version)


class RequirementSet:
    """
    A class for managing optional dependencies in a requirements.txt.

    Parameters
    ----------
    set_name : str
        the name of the new configuration set
    config_option: str
        the string that will appear in cookiecutter.json
    config_defulat: Union[str, List[str]]
        the default value or list of possible values for the cookiecutter.json
        entry.
    include_str: str
        the string used to evaluate truth for this config option. for the
        requirements to be included, cookiecutter.config_option == include_str.
    packages: List[str]
        the list of pinned packages to include for this set.

    Example
    -------

        ytReqs = RequirementSet(set_name='yt',
                        config_option="include_yt_requirements",
                        config_default="y",
                        include_str="y",
                        packages=["yt>=4.0.1", "h5py>=3.4.0", "pooch>=1.5.1", "pandas>=1.3.3"])

    creates an expanded requirement set for yt (yt plus useful optional dependencies).

    When the template is generated via write_template(), the cookiecutter.json
    will have an entry:

        "include_yt_requirements": "y"


    """

    def __init__(self,
                 set_name: str,
                 config_option: str,
                 config_default: Union[str, List[str]],
                 include_str: str,
                 packages: List[str]):

        self.set_name = set_name
        self.config_option = config_option
        self.config_default = self._validate_config_default(config_default)
        self.packages = self._validate_packages(packages)
        self.include_str = include_str

    def _validate_config_default(self, config_default):
        if type(config_default) == list:
            config_default = str(config_default)
        return config_default

    def _validate_packages(self, package_list):
        for package in package_list:
            if _validate_package_string(package) is False:
                raise ValueError(f"{package} is not pinned at a version")
        return package_list

    @property
    def template(self):
        t = "{%- if cookiecutter." + self.config_option + "|lower == '" + self.include_str + "' %}\n"
        for package in self.packages:
            t += package + "\n"
        t += "{%- endif %}\n"
        return t


ytReqs = RequirementSet(set_name='yt',
                        config_option="include_yt_requirements",
                        config_default="y",
                        include_str="y",
                        packages=["yt>=4.0.1", "h5py>=3.4.0", "pooch>=1.5.1", "pandas>=1.3.3"])


clickReqs = RequirementSet(set_name='click',
                           config_option="command_line_interface",
                           config_default=["Click", "Argparse", "No command-line interface"],
                           include_str="click",
                           packages=["Click>=7.0"])

requirement_sets = [ytReqs, clickReqs]

def write_template(reqfile: str, overwrite: bool = False):
    """
    writes a requirements file template

    Parameters
    ----------
    reqfile: str
        the requirements file
    overwrite: bool
        will overwrite existing file if found (default False)

    Note
    ----

    Duplicated requirements between sets are handled by the cookiecutter post_gen_project.py
    hook after a user makes their choices. Exact duplicates are consolidated, but conflicted
    duplicates (same package, different pinned versions) are simply flagged and the user
    must manually edit the requirements.txt file after using the template.
    """
    ch = CookieCutterHandler()

    if os.path.isfile(reqfile) and overwrite is False:
        raise FileExistsError(f"{reqfile} already exists, set overwrite=True to overwrite")

    with open(reqfile, "w") as fi:

        for req_set in requirement_sets:
            # update the cookiecutter.json entry
            ch[req_set.config_option] = req_set.config_default
            # write the requirements template
            fi.write(req_set.template)

    # write the updated cookiecutter json
    ch.json_dump()

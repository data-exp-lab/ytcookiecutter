"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

{%- if "stream" in cookiecutter.frontend_type|lower%}
from .'{{ cookiecutter.project_slug}}' import load
{%- endif %}

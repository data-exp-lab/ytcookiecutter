"""Console script for {{cookiecutter.project_slug}}."""

import sys
import click
from . import stream_template, skeleton_template, requirements_template
import os

@click.group()
def main():
    pass


@main.command()
@click.option("--subdir", type=str, default=None, help="the directory to write to")
def build_stream(subdir):
    """generate the stream templates"""

    stream_types = ["uniform grid",
                    "amr grids",
                    "particles",
                    "octree",
                    "hexahedral mesh",
                    "unstructured mesh"]

    if subdir is None:
        subdir = os.path.join('{{cookiecutter.project_slug}}',
                              '{{cookiecutter.project_slug}}',
                              "frontend_templates",
                              "stream")
    filename = '{{cookiecutter.project_slug}}.py'
    stream_template.write_template(stream_types, filename=filename, subdir=subdir)


@main.command()
@click.option("--subdir", type=str, default=None, help="the directory to write to")
def build_skeleton(subdir):
    """generate the AMR skeleton template"""

    if subdir is None:
        subdir = os.path.join('{{cookiecutter.project_slug}}',
                              '{{cookiecutter.project_slug}}',
                              "frontend_templates",
                              "skeleton")
    skeleton_template.write_template(subdir=subdir)


@main.command()
@click.option("--subdir", type=str, default='{{cookiecutter.project_slug}}', help="the directory to write to")
@click.option("--reqfile", type=str, default='requirements.txt', help="the requirements filename")
@click.option("--overwrite", type=bool, default=False, help="overwrite if file exists?")
def build_requirements(subdir, reqfile, overwrite):
    """generate the requirements template"""
    reqfile = os.path.join(subdir, reqfile)
    requirements_template.write_template(reqfile=reqfile, overwrite=overwrite)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

"""Console script for {{cookiecutter.project_slug}}."""

import sys
import click
from .stream_template import write_template
import os

@click.group()
def main():
    pass


@main.command()
@click.option("--filename", type=str, default=None, help="the filename to write to")
def stream_template(filename):
    """generate the stream templates"""

    stream_types = ["uniform grid",
                    "amr grids",
                    "particles",
                    "octree",
                    "hexahedral mesh",
                    "unstructured mesh"]

    if filename is None:
        filename = os.path.join('{{cookiecutter.project_slug}}',
                                '{{cookiecutter.project_slug}}',
                                '{{cookiecutter.project_slug}}.py')
    write_template(stream_types, filename=filename)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

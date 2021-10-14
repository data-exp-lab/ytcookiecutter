#!/usr/bin/env python
import os
from shutil import copyfile, rmtree
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(get_project_filepath(filepath))


def get_project_filepath(filepath):
    return os.path.join(PROJECT_DIRECTORY, filepath)


def _parse_package(version_string):
    for op in [">=", "==", "<=", "<", ">"]:
        if op in version_string:
            package = version_string.split(op)[0]
            return package
    # no version pin in version_string, just return it
    return version_string


def _check_reqs_for_duplicates():

    reqfile = os.path.join(PROJECT_DIRECTORY, "requirements.txt")
    with open(reqfile, "r") as fi:
        all_reqs = [pack for pack in fi.read().split("\n") if pack != '']

    packages = []  # list of package names, no versions
    duplicates = []  # list of duplicated package names, no versions
    fullpackages = []  # just a copy of all_reqs if there are no duplicates

    # first get the list of duplicated packages
    warn_dupes = False
    rewrite_reqs = False
    for req in all_reqs:
        package_name = _parse_package(req)
        if req in fullpackages:
            # this is an EXACT duplicate, just leave it off
            rewrite_reqs = True
            continue
        else:
            # not an exact duplicate
            fullpackages.append(req)

        # the package name may still be a duplicate
        if package_name in packages:
            duplicates.append(package_name)
            warn_dupes = True
            rewrite_reqs = True
        packages.append(package_name)

    if warn_dupes:
        print("Warning: duplicate requirement found, check requirements.txt "
                      "in your new package directory")

    # if there are duplicates, copy over reqs but flag the duplicates and
    # write back out to the requirements file.
    if duplicates:
        reqs = []
        for req in fullpackages:
            if _parse_package(req) in duplicates:
                reqs.append(req + " <<< duplicate")
            else:
                reqs.append(req)
        with open(reqfile, "w") as fi:
            fi.write("\n".join(reqs))
    elif rewrite_reqs:
        with open(reqfile, "w") as fi:
            fi.write("\n".join(fullpackages))


def copy_frontend_template(dest_dir, template_dir, fe_type):

    source_dir = os.path.join(template_dir, fe_type)
    init_contents = None
    for fi in os.listdir(source_dir):
        if fi == "__init__.py":
            with open(os.path.join(source_dir, fi), "r") as fhandle:
                init_contents = "\n" + fhandle.read() + "\n"
        else:
            copyfile(os.path.join(source_dir, fi),
                     os.path.join(dest_dir, fi))
    return init_contents


def _select_frontend(project_dir):
    # frontend selection: copies over files from frontend_templates, merges
    # the __init__.py file and deletes the frontend_templates directory

    fe_type = '{{ cookiecutter.frontend_type }}'.lower()
    template_dir = os.path.join(project_dir, "frontend_templates")
    init_contents = None
    if fe_type == "amr skeleton":
        init_contents = copy_frontend_template(project_dir, template_dir, "skeleton")
    elif "stream" in fe_type:
        init_contents = copy_frontend_template(project_dir, template_dir, "stream")

    if init_contents is not None:
        with open(os.path.join(project_dir, "__init__.py"), "a") as fhandle:
            fhandle.write(init_contents)

    rmtree(template_dir)


if __name__ == '__main__':

    project_dir = '{{ cookiecutter.project_slug }}'

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join(project_dir, 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    _check_reqs_for_duplicates()
    _select_frontend(project_dir)


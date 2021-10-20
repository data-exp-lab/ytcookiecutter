from github import Github
from abc import ABC, abstractmethod
import os
from typing import Union
from pathlib import Path, PosixPath
from .custom_types import filelike
from .utilities import _sanitize_path


class GithubSkeleton(ABC):

    def __init__(self, subdir: filelike, files_to_copy: list, dest_dir: filelike):
        self.subdir = _sanitize_path(subdir)
        self.dest_dir = _sanitize_path(dest_dir)
        self.files_to_copy = files_to_copy
        self.file_content = self._fetch()

    def _fetch(self):
        g = Github()
        ytrepo = g.get_repo("yt-project/yt")

        file_content = {}
        for fi in self.files_to_copy:
            file_path = str(self.subdir.joinpath(fi))
            repo_file = ytrepo.get_contents(file_path)
            fi_contents = repo_file.decoded_content.decode('ascii')
            file_content[fi] = self._sanitize_file_contents(fi_contents)

        return file_content

    @abstractmethod
    def _sanitize_file_contents(self, fi_contents: str) -> str:
        pass

    def write(self):
        for fi, fi_contents in self.file_content.items():
            fullfi = self.dest_dir.joinpath(fi)
            with open(fullfi, "w") as fhandle:
                fhandle.write(fi_contents)


class AMRSkeleton(GithubSkeleton):

    def __init__(self, dest_dir: filelike = None):
        subdir = "yt/frontends/_skeleton/"
        files = ["api.py",
                 "data_structures.py",
                 "definitions.py",
                 "fields.py",
                 "io.py",
                 "misc.py",
                 ]

        if dest_dir is None:
            dest_dir = os.path.join('{{cookiecutter.project_slug}}',
                                    "frontend_templates",
                                    "skeleton")

        super().__init__(subdir, files, dest_dir)

    def _sanitize_file_contents(self, fi_contents: str) -> str:
        fe_name = "{{ cookiecutter.frontend_name }}"
        fi_contents = fi_contents.replace("Skeleton", fe_name)
        fe_name = "{{ cookiecutter.frontend_name|lower }}"
        fi_contents = fi_contents.replace("skeleton", fe_name)
        return fi_contents

    def write(self):
        super().write()

        # copy over the api file into an init file
        init_fi = self.dest_dir.joinpath("__init__.py")
        with open(init_fi, "w") as fhandle:
            fhandle.write(self.file_content["api.py"])


def write_template(subdir: filelike = "./"):
    skele = AMRSkeleton(dest_dir=subdir)
    skele.write()

import yt
from inspect import getfullargspec, getdoc
import os
from . import metatemplater
from .custom_types import filelike
from .utilities import _sanitize_path
from typing import List

class StreamTemplate:

    def __init__(self, stream_type: str, include_docstring: bool=False):
        self.template_name = "stream.py"
        self.stream_type = stream_type
        self.stream_type_ = stream_type.replace(" ", "_")
        self.frontend_type_str = "stream: " + stream_type
        self.load_func_str = f"load_{self.stream_type_}"
        self.func_handle = getattr(yt.loaders, self.load_func_str)
        self.include_docstring = include_docstring
        self.docstr = getdoc(self.func_handle)
        self.funcargs = getfullargspec(self.func_handle)

        # number of args and kwargs for this load function:
        self.n_args = len(self.funcargs.args) - len(self.funcargs.defaults)
        self.n_kwargs = len(self.funcargs.args) - self.n_args
        # the type of each function's default argument:
        self.default_types = [type(fd) for fd in self.funcargs.defaults]

        # generate the code for this load function
        self.template = metatemplater.get_template(self.template_name)
        self.filled_template = self._fill_template()

    def _fill_template(self):

        func_args = []
        kwarg_dict = {}
        for iarg, argname in enumerate(self.funcargs.args):
            if iarg > self.n_args - 1:
                # its a keyword argument
                nkw = iarg - self.n_args

                def_val = self.funcargs.defaults[nkw]
                if self.default_types[nkw] == str:
                    def_val = f"'{def_val}'"

                # its a keyword argument
                kwarg_dict[argname] = def_val
            else:
                func_args.append(argname)

        rs = self.template.render(load_func=self.load_func_str,
                                  frontend_type_str=self.frontend_type_str,
                                  argnames=func_args,
                                  kwarg_dict=kwarg_dict,
                                  include_docstring=self.include_docstring,
                                  docstring=self.docstr)
        return rs

    def write(self, filename: filelike, mode="w"):
        with open(filename, mode) as fi:
            self.write_to_handle(fi)

    def write_to_handle(self, fhandle):
        fhandle.write(self.filled_template)


def indent_str(in_str: str, n: int = 1):
    return " " * 4 * n + in_str


def concat_stream_types(stream_types: list) -> list:
    stream_code = ''
    for s in stream_types:
        stemp = StreamTemplate(s)
        stream_code += stemp.filled_template +"\n"
    return stream_code


def write_template(stream_types: List[str],
                   filename: filelike = "stream_template.py",
                   subdir: filelike = "./"):

    stream_code = concat_stream_types(stream_types)

    subdir = _sanitize_path(subdir)
    fullfi = subdir.joinpath(filename)
    with open(fullfi, "w") as fi:
        fi.write(stream_code)

    initfi = subdir.joinpath("__init__.py")
    with open(initfi, "w") as fi:
        fi.write("from .{{ cookiecutter.project_slug}} import load")


if __name__ == "__main__":

    stypes = ["uniform grid",
              "amr grids",
              "particles",
              "octree",
              "hexahedral mesh",
              "unstructured mesh"]

    write_template(stypes)










import yt
from inspect import getfullargspec, getdoc
import os


class StreamTemplate:

    def __init__(self, stream_type: str, include_docstring: bool=False):
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
        self.code = self._gen_code()

    def _gen_code(self) -> list:
        code = []
        code.append('{%- if cookiecutter.frontend_type|lower == "' + self.frontend_type_str + '" %}' + "\n")
        code.append(f"from yt.loaders import {self.load_func_str}\n\n")
        code.append("def load(filename: str):\n\n")
        code.append(indent_str("# write code to load data from filename into memory!\n\n"))

        for iarg, argname in enumerate(self.funcargs.args):

            if iarg > self.n_args - 1:
                # its a keyword argument
                nkw = iarg - self.n_args

                if nkw == 0:
                    code.append("\n"+indent_str("# set or delete optional kwargs\n"))
                def_val = self.funcargs.defaults[nkw]
                if self.default_types[nkw] == str:
                    def_val = f"'{def_val}'"
                argstr = f"{argname} = {def_val}\n"
            else:
                argstr = f"{argname} = ????????\n"
            code.append(indent_str(argstr))

        code.append("\n"+indent_str("# call the stream data loader.\n"))
        code.append(indent_str(f"ds = {self.load_func_str}(\n"))
        for iarg, argname in enumerate(self.funcargs.args):

            if iarg > self.n_args - 1:
                # its a keyword argument
                code.append(indent_str(f"{argname}={argname},\n", n=2))
            else:
                code.append(indent_str(f"{argname},\n", n=2))
        code.append(indent_str(")\n\n", n=2))
        code.append("\n" + indent_str("# return the in-memory ds\n"))
        code.append(indent_str("return ds\n"))
        if self.include_docstring:
            code.append(f"\n# description of {self.load_func_str} for convenience:\n")
            code.append('"""\n')
            code.append(self.docstr)
            code.append('\n"""\n')
        code.append('{%- endif %}' + "\n\n")

        return code

    def write(self, filename: str, mode="w"):
        with open(filename, mode) as fi:
            self.write_to_handle(fi)

    def write_to_handle(self, fhandle):
        for c in self.code:
            fhandle.write(c)


def indent_str(in_str: str, n: int = 1):
    return " " * 4 * n + in_str


def concat_stream_types(stream_types: list) -> list:
    stream_code = []
    for s in stream_types:
        stemp = StreamTemplate(s)
        stream_code += stemp.code
    return stream_code


def write_template(stream_types: list,
                   filename: str = "stream_template.py",
                   subdir: str = "./"):

    stream_code = concat_stream_types(stream_types)

    fullfi = os.path.join(subdir, filename)
    with open(fullfi, "w") as fi:
        for line in stream_code:
            fi.write(line)

    initfi = os.path.join(subdir, "__init__.py")
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










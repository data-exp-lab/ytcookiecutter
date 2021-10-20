from pathlib import Path, PosixPath
from .custom_types import filelike


def _sanitize_path(path_or_str: filelike) -> PosixPath:
    if type(path_or_str) == str:
        return Path(path_or_str)
    elif type(path_or_str) == PosixPath:
        return path_or_str
    else:
        raise ValueError("path should be type str or Path")

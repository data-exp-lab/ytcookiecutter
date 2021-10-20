from dxlcookiecutter.skeleton_template import write_template
from pathlib import Path

def test_skeleton():

    # note: don't want to run tests fetching from github due to api rate limits.
    # d = tmp_path / "skelebone"
    # d.mkdir()
    # write_template(d)


    # just that the currently built template is as expected
    files = ["api.py",
             "data_structures.py",
             "definitions.py",
             "fields.py",
             "io.py",
             "misc.py",
             ]

    subdir = Path("{{cookiecutter.project_slug}}")
    subdir = subdir.joinpath("{{cookiecutter.project_slug}}")
    subdir = subdir.joinpath("frontend_templates")
    subdir = subdir.joinpath("skeleton")
    for fi in files:
        skelebone = subdir.joinpath(fi)
        assert skelebone.is_file()  # bone in body
        innards = skelebone.read_text()
        assert "skeleton" not in innards.lower()


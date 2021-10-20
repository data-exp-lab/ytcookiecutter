from ytcookiecutter.stream_template import write_template


def test_stream_template(tmp_path):
    d = tmp_path / "stream"
    d.mkdir()

    stypes = ["uniform grid",
              "amr grids",
              "particles",
              "octree",
              "hexahedral mesh",
              "unstructured mesh"]

    write_template(stypes, filename="stream_fi.py", subdir=d)

    stream_fi = d.joinpath("stream_fi.py")
    assert stream_fi.is_file()

    stream_conents = stream_fi.read_text()
    for styp in stypes:
        load_func = "load_" + styp.replace(" ","_")
        assert load_func in stream_conents


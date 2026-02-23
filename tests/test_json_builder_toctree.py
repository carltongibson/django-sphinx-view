import json
from pathlib import Path

from sphinx.cmd.build import main as sphinx_build


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _build_json(src: Path, out: Path, doctrees: Path) -> int:
    return sphinx_build(
        [
            "-E",
            "-a",
            "-b",
            "json",
            str(src),
            str(out),
            "-d",
            str(doctrees),
        ]
    )


def test_toctree_serialized_as_string_in_fjson(tmp_path: Path) -> None:
    src = tmp_path / "src"
    out = tmp_path / "_build" / "json"
    doctrees = tmp_path / "_build" / "doctrees"
    src.mkdir(parents=True)

    _write(
        src / "conf.py",
        "extensions = ['sphinx_view']\nproject = 'test-project'\nroot_doc = 'index'\n",
    )
    _write(
        src / "index.rst",
        "Home\n====\n\n.. toctree::\n   :maxdepth: 1\n\n   changelog\n",
    )
    _write(src / "changelog.rst", "Changelog\n=========\n\nEntry.\n")

    assert _build_json(src, out, doctrees) == 0

    data = json.loads((out / "changelog.fjson").read_text(encoding="utf-8"))
    assert "toc" in data
    assert "toctree" in data
    assert isinstance(data["toctree"], str)
    assert data["toctree"] != ""


def test_toctree_key_present_even_without_toctree_directive(tmp_path: Path) -> None:
    src = tmp_path / "src"
    out = tmp_path / "_build" / "json"
    doctrees = tmp_path / "_build" / "doctrees"
    src.mkdir(parents=True)

    _write(
        src / "conf.py",
        "extensions = ['sphinx_view']\nproject = 'test-project'\nroot_doc = 'index'\n",
    )
    _write(src / "index.rst", "Home\n====\n\nNo toctree here.\n")

    assert _build_json(src, out, doctrees) == 0

    data = json.loads((out / "index.fjson").read_text(encoding="utf-8"))
    assert "toctree" in data
    assert isinstance(data["toctree"], str)
    assert data["toctree"] == ""

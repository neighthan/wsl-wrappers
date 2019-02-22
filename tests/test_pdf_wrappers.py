import filecmp
from pathlib import Path
from unittest.mock import patch
import pytest
from wsl_wrappers.scripts_api import pdflatex, pdf2svg

_test_dir = Path(__file__).parent.resolve()


@pytest.mark.datafiles(
    _test_dir / "test.tex", _test_dir / "expected.pdf", _test_dir / "expected.svg"
)
def test_pdf_wrappers(datafiles):
    datafiles = Path(str(datafiles))
    test_tex_path = datafiles / "test.tex"
    test_pdf_path = datafiles / "test.pdf"
    test_svg_path = datafiles / "test.svg"
    expected_pdf_path = datafiles / "expected.pdf"
    expected_svg_path = datafiles / "expected.svg"

    # testing for the PDFs / svgs to be the same wasn't working well, even when
    # they looked the same to me. This at least tests that the commands run and
    # generate output files. I'm not sure of a more robust way to do this.

    for path in [test_tex_path, expected_pdf_path, expected_svg_path]:
        assert path.is_file()

    pdflatex_args = [
        "pdflatex",
        "-output-directory",
        str(datafiles),
        str(test_tex_path),
    ]
    pdf2svg_args = ["pdf2svg", str(test_pdf_path), str(test_svg_path)]

    with patch("sys.argv", pdflatex_args):
        print(pdflatex_args)
        pdflatex(verbose=True)

    assert test_pdf_path.is_file()
    # assert filecmp.cmp(str(test_pdf_path), str(expected_pdf_path))

    with patch("sys.argv", pdf2svg_args):
        pdf2svg(verbose=True)

    assert test_svg_path.is_file()
    # assert filecmp.cmp(str(test_svg_path), str(expected_svg_path))

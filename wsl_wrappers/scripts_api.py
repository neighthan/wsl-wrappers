from .utils import run_command
from ._scripts.pdf2svg import get_command_pdf2svg
from ._scripts.pdflatex import get_command_pdflatex


def pdf2svg(verbose: bool = False):
    cmd = get_command_pdf2svg()
    if verbose:
        print(cmd)
    run_command(cmd)


def pdflatex(verbose: bool = False):
    cmd = get_command_pdflatex()
    if verbose:
        print(cmd)
    run_command(cmd)

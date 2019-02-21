from .utils import run_command
from ._scripts.pdf2svg import get_command_pdf2svg
from ._scripts.pdflatex import get_command_pdflatex


def pdf2svg():
    run_command(get_command_pdf2svg())


def pdflatex():
    run_command(get_command_pdflatex())

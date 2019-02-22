from pathlib import Path
from subprocess import run
from .utils import run_command
from ._scripts.pdf2svg import get_command_pdf2svg
from ._scripts.pdflatex import get_command_pdflatex
from ._scripts.install_wsl_git import install_wsl_git


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


def git(verbose: bool = False):
    git_cmd_path = Path(__file__).parent / "_scripts" / "git.cmd"
    run(str(git_cmd_path), shell=True)


def install_wgit(verbose: bool = False):
    install_wsl_git(verbose=verbose)

# remember to add .PY to PATHEXT so you can call this without the extension

from argparse import ArgumentParser
from typing import List
from ..utils import get_wsl_path


def get_command_pdf2svg() -> List[str]:
    parser = ArgumentParser()
    parser.add_argument("pdffile", type=get_wsl_path, help="path to the pdf file to convert")
    parser.add_argument("svgfile", type=get_wsl_path)
    parser.add_argument("page_number", nargs="?", default="")

    args = parser.parse_args()
    cmd = ["wsl", "pdf2svg", args.pdffile, args.svgfile]
    cmd += [args.page_number] if args.page_number else []
    return cmd

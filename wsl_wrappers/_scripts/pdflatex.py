import sys
from argparse import ArgumentParser
from typing import List
from ..utils import get_wsl_path


def get_command_pdflatex() -> List[str]:
    # TODO - this one isn't done very well...
    # the last arg is the filename *unless* it's a list of commands, the
    # first of which starts with \. It might be possible that \ is included
    # in the args somewhere else, though? This works for now, but it's hacky
    # at best and probably fails sometimes

    args = sys.argv[1:]
    last_arg_is_fname = True
    for arg in args:
        if arg.startswith("\\"):
            last_arg_is_fname = False
            break

    if last_arg_is_fname:
        print(args[-1])
        args[-1] = get_wsl_path(args[-1])

    for idx, arg in enumerate(args):
        if arg.strip() == "-output-directory":
            args[idx + 1] = get_wsl_path(args[idx+1])
            break

    cmd = ["wsl", "pdflatex"] + args
    return cmd

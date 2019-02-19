import sys
from argparse import ArgumentParser
from wsl_wrappers import get_wsl_path, run_command


def get_command_pdflatex() -> str:
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

    cmd = ["wsl", "pdflatex"] + args
    return cmd


if __name__ == "__main__":
    run_command(get_command_pdflatex())

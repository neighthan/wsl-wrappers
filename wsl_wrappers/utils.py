import os
from pathlib import Path
from subprocess import run
from typing import List


def get_wsl_path(win_path: str) -> str:
    win_path = Path(win_path)
    if not win_path.is_absolute():
        win_path = Path(os.getcwd()) / win_path

    win_path = str(win_path.resolve()).replace("\\", "\\\\")
    # note that wslpath might have issues with manually mounted drives
    # see https://github.com/hangxingliu/wslgit
    result = run("wsl wslpath -u".split(" ") + [f"{win_path}"], capture_output=True)
    wsl_path = result.stdout.decode().strip()
    return wsl_path


def get_win_path(wsl_path: str) -> str:
    # TODO - wsl_path must be absolute for now; if it's not, then you might need
    # to make a call to wsl to have python there resolve it
    result = run("wsl wslpath -w".split(" ") + [f"{wsl_path}"], capture_output=True)
    win_path = result.stdout.decode().strip()
    return win_path


def run_command(cmd: List[str]) -> None:
    """
    Run the given command, printing output / errors.

    :param cmd: a command that can be passed into `subprocess.run`
      `subprocess.run` handles escaping spaces in paths, so you don't need
      to do this manually. Strangely, I've received errors when quoting paths
      which were resolved by not quoting them, so I would recommended to use
      any paths directly.
    """
    result = run(cmd, capture_output=True)
    stdout = result.stdout.decode().strip()
    stderr = result.stderr.decode().strip()

    if stdout:
        print(stdout)

    if stderr:
        print(stderr)
        print(f'Command was `{" ".join(cmd)}`.')

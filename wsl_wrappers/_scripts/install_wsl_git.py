from pathlib import Path
from subprocess import run
from urllib.request import urlopen

# updated 2-22-19
_wsl_git_url = "https://raw.githubusercontent.com/hangxingliu/wslgit/e28863408ed5054e44c163db4c11d2ddd3d0cc6c/wslgit.sh"
_git_cmd_url = "https://raw.githubusercontent.com/hangxingliu/wslgit/e28863408ed5054e44c163db4c11d2ddd3d0cc6c/git.bat"


def install_wsl_git(verbose: bool = False):
    git_cmd = urlopen(_git_cmd_url).read()
    git_cmd_path = Path(__file__).parent / "git.cmd"
    git_cmd_path.write_bytes(git_cmd)
    if verbose:
        print(f"Saved Windows git command to {git_cmd_path}.")

    wsl_git = urlopen(_wsl_git_url).read()
    wsl_git_path = Path(".") / "wslgit.sh"
    wsl_git_path.write_bytes(wsl_git)
    if verbose:
        print(f"Saved WSL git command to {wsl_git_path}.")

    run(["wsl", "sudo", "mv", "./wslgit.sh", "/usr/bin"])
    if verbose:
        print(f"Moved WSL git command to /usr/bin/wslgit.sh.")

import toml
from pathlib import Path
from .utils import get_win_path, get_wsl_path, run_command

# pyproject = toml.load(str(Path(__file__).parents[1] / "pyproject.toml"))
# __version__ = pyproject["tool"]["poetry"]["version"]
# del pyproject

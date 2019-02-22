import invoke
import platform
from pathlib import Path
from tempfile import TemporaryDirectory


def _fixed_run(ctx, cmd: str, *args, **kwargs):
    if platform.system() != "Windows":
        return ctx._old_run(cmd, *args, **kwargs)

    with TemporaryDirectory() as tmp_dir:
        tmp_file = Path(tmp_dir) / "tmp.bat"
        tmp_file.write_text("@echo off\r\n" + cmd)
        return ctx._old_run(str(tmp_file), *args, **kwargs)

invoke.Context._old_run = invoke.Context.run
invoke.Context.run = _fixed_run

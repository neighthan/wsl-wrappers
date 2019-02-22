[![Build Status](https://travis-ci.org/neighthan/wsl-wrappers.svg?branch=master)](https://travis-ci.org/neighthan/wsl-wrappers)

# WSL Wrappers

This repo contains a set of wrappers that make it easier to call commands in Windows Subsystem for Linux (WSL) from Windows. Basically, they are wrappers that do a small amount of path conversion using `wslpath` and then pass the arguments on to the real command in WSL using `wsl`.

## List of Wrappers
* `pdflatex`
* `pdf2svg`

## Usage

```
pip install wsl-wrappers
```

The script wrappers are automatically put in your Python scripts directory (e.g. `%USERPROFILE%\Anaconda\Scripts`). You should be able to call them directly from the command line.

## Related Work
* [`wslgit`][wslgit] is an excellent project for using WSL's `git` from Windows which also works well with VS Code.

[wslgit]: https://github.com/hangxingliu/wslgit

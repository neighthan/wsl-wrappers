import setuptools
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

version = {}
version_file = Path(__file__).parent / "wsl_wrappers/_version.py"
exec(version_file.read_text(), version)

setuptools.setup(
    name="wsl_wrappers",
    version=version["__version__"],
    author="Nathan Hunt",
    author_email="neighthan.hunt@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/neighthan/wsl_wrappers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)

scripts_dir = Path(__file__).parent / "scripts"
# TODO - prompt user, if they say yes, add to path automatically
print(f"Add {scripts_dir} to your PATH to be able to use them.")

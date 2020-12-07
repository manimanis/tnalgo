import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tnalgo",
    version="1.0.4",
    description="A set of algorithmic functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/manimanis/tnalgo",
    author="Mohamed Anis MANI",
    author_email="manimohamed@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["tnalgo"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tnalgo=tnalgo.__main__:main",
        ]
    },
)

  
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="lsmake",
    version="1.0.3",
    description="Create list",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SumirVats2003/lsmake",
    author="Sumir Vats",
    author_email="sumirvats@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["lsmake"],
    include_package_data=True,
    install_requires=[],
    # entry_points={
    #     "console_scripts": [
    #         "lsmake=lsmake.__main__:main",
    #     ]
    # },
)

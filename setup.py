import os
from setuptools import setup


setup(
    name = "datatypes",
    version = "0.0.1",
    author = "Javis Sullivan",
    author_email = "javissullivan@gmail.com",
    description = "Abstract data types.",
    license = "BSD",
    keywords = ["datatypes"],
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "robotc-wrapper",
    packages = ["robotc"],
    version = "0.4",
    description = "A Python 2.7 wrapper for RobotC and Vex PIC robot",
    author = "James Albert",
    author_email = "james.albert72@gmail.com",
    url = "https://github.com/jamesalbert/robotc-wrapper-python",
    download_url = "git@github.com:jamesalbert/robotc-wrapper-python.git",
    keywords = ["robot", "vex", "c"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description=open('README').read(),
)

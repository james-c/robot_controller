import os

from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "robot_controller",
    version = "0.0.1",
    author = "James Cunningham",
    author_email = "j.a.cunningham@gmail.com",
    description = ("Web based controller for a mobile robot."),
    license = "MIT",
    packages=find_packages(exclude=['docs', 'tests']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Robot Framework"
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['Flask']
)

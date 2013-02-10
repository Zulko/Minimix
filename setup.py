#!/usr/bin/env python
"""Distutils based setup script for SymPy.

This uses Distutils (http://python.org/sigs/distutils-sig/) the standard
python mechanism for installing packages. For the easiest installation
just type the command (you'll probably need root privileges for that):

python setup.py install

This will install the library in the default location. For instructions on
how to customize the install procedure read the output of:

python setup.py --help install

In addition, there are some other commands:

python setup.py clean -> will clean all trash (*.pyc and stuff)
python setup.py test -> will run the complete test suite
python setup.py bench -> will run the complete benchmark suite
python setup.py audit -> will run pyflakes checker on source code

To get a full list of avaiable commands, read the output of:

python setup.py --help-commands

Or, if all else fails, feel free to write to the sympy list at
sympy@googlegroups.com and ask for help.
"""

long_description =  'Minimix is a minimalistic program that lets you \
assign one sound to each key of you typing keyboard, in order to use \
your it as a mix table or as a proper musical instrument.'

from distutils.core import setup
setup(name='minimix',
      version='1.0',
      author='Zulko 2013',
    description='Music and mixing on the keyboard',
    long_description=long_description,
    license='BSD',
    keywords="music piano mixtable",
    packages=['minimix'] )

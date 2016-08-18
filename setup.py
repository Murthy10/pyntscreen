#!/usr/bin/env python

from distutils.core import setup

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(name='pyntscreen',
      version='1.0',
      description='a small tool to take screenshots along your mouse cursor movement',
      author='Samuel Kurath',
      author_email='samuel.kurath@gmail.com',
      packages=['distutils', 'distutils.command'],
      install_requires=REQUIREMENTS,
      )

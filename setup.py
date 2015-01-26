#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='cronfilter',
      version='1.0.0',
      description='Filter a list of dates based on a cron expression',
      author='Erskin Cherry',
      author_email='erskin@eldritch.org',
      url='https://github.com/frobnic8/cronfilter',
      download_url='https://github.com/frobnic8/cronfilter/tree/master/dist',
      py_modules=['cronfilter'],
      entry_points={'console_scripts': ['cronfilter = cronfilter:main']},
      long_description=open('README.md').read(),
      provides=['cronfilter'],
      install_requires=['croniter >= 0.3.5'],
)

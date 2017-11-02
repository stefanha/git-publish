#!/usr/bin/env python
from distutils.core import setup

setup(name='git-publish',
      version='1.4.0',
      description='Patch series management tool for git',
      long_description='Prepare and store patch series as git tags',
      url='https://github.com/stefanha/git-publish/',
      author='Stefan Hajnoczi',
      author_email='stefanha@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Topic :: Software Development',
      ],
      keywords='git patch series management',
      scripts=['git-publish'],
)

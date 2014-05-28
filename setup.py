#!/usr/bin/env python

from setuptools import setup
import couchbase

setup(
      name="py-ace",
      version= '0.0.3',
      description="make all python script as c extention with cython",
      long_description=open("README.txt").read(),
      author="MaxiL",
      author_email="maxil@interserv.com.tw",
      maintainer="MaxiL",
      maintainer_email="maxil@interserv.com.tw",
      url="",
      download_url="https://github.com/maxi119/py-ace",
      packages=["pyace"],
      install_requires=[
      	'cython',
      ],
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Topic :: Security",        
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])


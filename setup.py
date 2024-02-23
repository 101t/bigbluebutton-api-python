#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='bigbluebutton_api_python',
      version='0.0.12',
      description='Python library that provides access to the API of BigBlueButton',
      author='Tarek Kalaji, Yunkai Wang, Hicham Dachir',
      author_email='yunkai.wang@blindsidenetworks.com',
      url='https://github.com/yunkaiwang/bigbluebutton-api-python',
      packages=find_packages(),
      install_requires=[
          'jxmlease'
      ],
)

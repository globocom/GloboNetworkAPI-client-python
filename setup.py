# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = __import__('networkapiclient').VERSION

setup(
    name='GloboNetworkAPI',
    version=version,
    description='GloboNetworkAPI Client Python',
    long_description='Python implementation of a client library for GloboNetworkAPI',
    keywords='network GloboNetwork GloboNetworkAPI',
    author='Marcus Vinicius Gonçalves Cesário',
    author_email='marcus.vinicius@corp.globo.com',
    url='https://github.com/globocom/GloboNetworkAPI-client-python',
    license='LICENSE.txt',
    install_requires=[
        'requests==2.10.0',
    ],
    packages=find_packages(),
)

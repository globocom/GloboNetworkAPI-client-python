# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import os.path

version = __import__('networkapiclient').VERSION

base_path = os.path.abspath(os.path.join(__file__, '..'))

setup(
    name='GloboNetworkAPI',
    version=version,
    description='GloboNetworkAPI Client Python',
    long_description=open(os.path.join(base_path, 'README.rst')).read(),
    keywords='network GloboNetwork GloboNetworkAPI',
    author='Marcus Vinicius Gonçalves Cesário',
    author_email='marcus.vinicius@corp.globo.com',
    url='https://github.com/globocom/GloboNetworkAPI-client-python',
    license='LICENSE.txt',
    install_requires=[
        'requests==2.4.3',
    ],
    packages=find_packages(),
)

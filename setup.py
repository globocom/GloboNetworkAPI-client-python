from setuptools import setup, find_packages

version = '0.2'

setup(
   name = 'GloboNetworkAPI',
   version = version,
   description = 'GloboNetworkAPI Client Python',
   long_description = open('README.rst').read(),
   keywords = 'network GloboNetwork GloboNetworkAPI',
   author = 'Marcus Vinicius Gonçalves Cesário',
   author_email = 'marcus.vinicius@corp.globo.com',
   url = 'https://github.com/globocom/GloboNetworkAPI-client-python',
   license = 'LICENSE.txt',
   packages = find_packages(),
)

# Makefile for globonetworkapi-client-python
VERSION=$(shell python -c 'import networkapiclient; print(networkapiclient.VERSION)')

# Pip executable path
PIP := $(shell which pip)

# GloboNetworkAPI project URL
GNETAPIURL := https://github.com/globocom/GloboNetworkAPI.git

# Local path to GloboNetworkAPI used in tests
GNETAPI_PATH := networkapi_test_project

help:
	@echo
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  docs       to create documentation files"
	@echo "  clean      to clean garbage left by builds and installation"
	@echo "  compile    to compile .py files (just to check for syntax errors)"
	@echo "  test       to execute all tests"
	@echo "  build      to build without installing"
	@echo "  install    to install"
	@echo "  dist       to create egg for distribution"
	@echo "  publish    to publish the package to PyPI"
	@echo "  setup      to setup environment locally to run project"
	@echo "  test_setup to setup test environment locally to run tests"
	@echo

clean:
	@echo "Cleaning project ..."
	@rm -rf build dist *.egg-info
	@rm -rf docs/_build
	@find . \( -name '*.pyc' -o -name '**/*.pyc' -o -name '*~' \) -delete

docs: clean
	@(cd docs && make html)

compile: clean
	@echo "Compiling source code..."
	@python -tt -m compileall .
	@pep8 --format=pylint --statistics networkapiclient setup.py

test:
	@make clean
	@echo "Starting tests..."
	@nosetests --rednose --nocapture --verbose --with-coverage --cover-erase \
		--cover-package=networkapiclient --where tests

unit:
	@make clean
	@echo "Starting tests..."
	@nosetests --rednose --nocapture --verbose --with-coverage --cover-erase \
		--cover-package=networkapiclient --where tests/unit

integration:
	@make clean
	@echo "Starting tests..."
	@nosetests --rednose --nocapture --verbose --with-coverage --cover-erase \
		--cover-package=networkapiclient --where tests/integration

functional:
	@make clean
	@echo "Starting tests..."
	@nosetests --rednose --nocapture --verbose --with-coverage --cover-erase \
		--cover-package=networkapiclient --where tests/functional

setup: requirements.txt
	$(PIP) install -r $^

test_setup: requirements_test.txt
	@echo "Installing test dependencies..."
	$(PIP) install -r $^
	@echo "Cloning GloboNetworkAPI..."
	@if [ ! -d $(GNETAPI_PATH) ]; then \
		git clone $(GNETAPIURL) $(GNETAPI_PATH); \
		cd $(GNETAPI_PATH) && git submodule update --init --recursive; \
	fi
	@echo "Running GloboNetworkAPI.."
	cd $(GNETAPI_PATH) && git pull origin master
	cd $(GNETAPI_PATH) && vagrant up --provider virtualbox

install:
	@python setup.py install

build:
	@python setup.py build

dist: clean
	@python setup.py sdist

update:
	@twine upload dist/*

publish: clean dist
	@echo 'Ready to release version ${VERSION}? (ctrl+c to abort)' && read
	@twine upload dist/*
	@git tag ${VERSION}
	@git push --tags

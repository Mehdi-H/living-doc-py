SHELL := /bin/bash
.SHELLFLAGS = -e -c
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
PYTHON_VERSION:=3.11.2

.DEFAULT_GOAL: help

.PHONY: help
help: USAGE.md
	@echo -e "Please use 'make <target>' where <target> is one of\n"
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = "(: |##)"}; {printf "- \033[36m%-30s\033[0m %s\n", $$2, $$3}' | sort

.PHONY: venv  ## 🥽 to setup a virtualenv for this project
venv:
	echo "[*] Using Python ${PYTHON_VERSION} 🐍 ..."
	poetry env use ${PYTHON_VERSION}

.PHONY: install-dependencies  ## to install all python dependencies
install-dependencies: venv
	poetry install

.PHONY: install-dependencies-run  ## to install python run dependencies
install-dependencies-run:
	poetry install --without dev

.PHONY: install-dependencies-dev  ## to install python dev dependencies
install-dependencies-dev:
	poetry install --with dev

.PHONY: install-dependencies-tests  ## to install python test dependencies
install-dependencies-tests:
	pip install .[tests]

.PHONY: unit-tests  ## to run unit tests 
unit-tests: clean
	poetry run pytest -v -m unit

.PHONY: func-tests  ## to run functional tests
func-tests: clean
	poetry run behave \
		-f html \
		-f steps \
		-o test-reports/behave-func-tests.html \
			living_doc/tests/features/

.PHONY: tests  ## to run all tests
tests: unit-tests func-tests

.PHONY: build  ## 🤸 to build a wheel distribution
build:
	poetry build

clean:
	rm -rf tests/__pycache__/ living_doc/__pycache__/ .pytest_cache/ build/ dist/ *.egg-info/ venv/

usage:
	echo -e "# Usage\n\n" > USAGE.md
	make -s help | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g" >> USAGE.md

.PHONY: format  ## ⚫ to format python code with Black formatter
format:
	poetry run black .

.PHONY: lint  ## 🍓 to lint python code
lint:
	poetry run ruff check .

demo:
	poetry run python living_doc/app.py demo
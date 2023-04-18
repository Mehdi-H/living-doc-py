SHELL := /bin/bash
.SHELLFLAGS = -e -c
.ONESHELL:
.SILENT:

.DEFAULT_GOAL: help

.PHONY: help
help: USAGE.md
	@echo -e "Please use 'make <target>' where <target> is one of\n"
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = "(: |##)"}; {printf "- \033[36m%-30s\033[0m %s\n", $$2, $$3}' | sort

.PHONY: install-dependencies-run  ## to install python run dependencies
install-dependencies-run:
	pip install -e .

.PHONY: install-dependencies-dev  ## to install python dev dependencies
install-dependencies-dev:
	pip install  .[dev]

.PHONY: install-dependencies-tests  ## to install python test dependencies
install-dependencies-tests:
	pip install .[tests]

.PHONY: install-dependencies-all  ## to install all python dependencies (run+tests)
install-dependencies-all: install-dependencies-run install-dependencies-tests install-dependencies-dev

.PHONY: unit-tests  ## to run unit tests 
unit-tests:
	pytest -v -m unit

clean:
	rm -rf tests/__pycache__/ build/

USAGE.md: Makefile
	echo -e "# Usage\n\n" > USAGE.md
	make help | head -n -1 | tail -n+2 | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g" >> USAGE.md

.PHONY: format  ## ⚫ to format python code with Black formatter
format:
	black .
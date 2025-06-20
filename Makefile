# ============================================================================
# Based on page: https://gist.github.com/prwhite/8168133
#
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# ============================================================================

##
## General
##

################################################################################
# Help target
################################################################################
# TODO: For now this is displaying '^' charater between target and description
help:: ## Help: Show this help text
		@gawk -vG=$$(tput setaf 2) -vR=$$(tput sgr0) ' \
			match($$0, "^(([^#:]*[^ :]) *:)?([^#]*)##([^#].+|)$$",a) { \
				if (a[2] != "") { printf "    make %s%-30s%s %s\n", G, a[2], R, a[4]; next } \
				if (a[3] == "") { print a[4]; next } \
					printf "\n%-36s %s\n","",a[4] \
			}' $(MAKEFILE_LIST)
		@echo "" # blank line at the end
.DEFAULT_GOAL := help

##
## Development
##

pip-update-all: ## Update pip and requirements.txt
pip-update-all: pip-update-pip pip-install-dependencies

pip-update-requirements: ## Update requirements.txt
		@echo "Updating requirements.txt"
		pip freeze > requirements.txt

pip-update-pip: ## Update pip package
		@echo "Updating pip"
		pip install --upgrade pip

pip-install-dependencies: ## Install PIP dependencies
		@echo "Installing dependencies"
		pip install -r requirements.txt

.PHONY: pip-install-linters
pip-install-linters: ## Install linters (flake8, pylint, mypy)
		@echo "Installing linters"
		pip install flake8 pytest

.PHONY: run-validation
run-validation:  ## Run flake8 lint checks
# stop the build if there are Python syntax errors or undefined names
		flake8 . --exclude=.venv,website \
			--count --select=E9,F63,F7,F82 \
			--show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
		flake8 . --exclude=.venv,website \
			--count --exit-zero --max-complexity=10 \
			--max-line-length=127 --statistics

##
## Publishing
##

.PHONY: sync-website-to-doc-folder
sync-website-to-doc-folder: ## Sync the website build to the docs folder
		@echo "Syncing website build to docs folder"
		rsync -av --delete \
			--filter='P CNAME' \
			--include='.*' \
			--include='*/' \
			website/build/html/ docs/

##
## Website / Blog
##

.PHONY: create-new-post
create-new-post: ## Create a new blog post
		@echo "Creating a new blog post"
		@python3 scripts/create-new-post.py

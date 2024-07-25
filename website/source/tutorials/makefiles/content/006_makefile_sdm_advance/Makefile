# ============================================================================
# Based on page: https://gist.github.com/prwhite/8168133
#
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
#
# Downloaded from:
#   https://raw.githubusercontent.com/marcinpraczko/collector/master/snippets/000-hardcoded/001-Makefile-self-describe-usage.txt
# ============================================================================

##
## General
##

################################################################################
# Help target
################################################################################
help:: ## Help: Show this help text
	@gawk -vG=$$(tput setaf 2) -vR=$$(tput sgr0) ' \
		match($$0, "^(([^#:]*[^ :]) *:)?([^#]*)##([^#].+|)$$",a) { \
			if (a[2] != "") { printf "    make %s%-30s%s %s\n", G, a[2], R, a[4]; next } \
			if (a[3] == "") { print a[4]; next } \
			printf "\n%-36s %s\n","",a[4] \
		}' $(MAKEFILE_LIST)
	@echo "" # blank line at the end
.DEFAULT_GOAL := help

.PHONY: display-info-file
display-info-file: ## Display INFO file
	cat "00Info.txt"

##
## Helper
##

.PHONY: bump-ver-patch
bump-ver-patch: ## Bump version - patch level
	bumpversion patch

.PHONY: clean
clean: ## Clean: Clean all temporary files
	$(MAKE) -C docs clean
	rm -fr *~


##
## Validate
##

.PHONY: validate
validate: ## Run ansible-lint validator
	@echo ""
	@echo "== Run ansible-lint =="
	ansible-lint tower-*.yml


.PHONY: validate-all
validate-all: ## Run all validation scripts
validate-all: galaxy_install validate galaxy_remove


##
## Operations
##

.PHONY: galaxy-install
galaxy-install: ## Ansible-galaxy: Install roles
	ansible-galaxy install -r roles/requirements.yml
	@echo ""
	@echo "== Installed roles =="
	ansible-galaxy list


.PHONY: galaxy-remove
galaxy-remove: ## Ansible-galaxy: Remove roles
	@echo "== Removing galaxy roles =="
	ansible-galaxy install -r roles/requirements.yml | \
		awk '{print $$2}' | xargs -I {} ansible-galaxy remove {}
	@echo ""
	@echo "== Result in 'roles' folder =="
	ls -la roles/

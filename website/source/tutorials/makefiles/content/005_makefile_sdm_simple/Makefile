# ============================================================================
# Based on page:
#   https://gist.github.com/prwhite/8168133
# 
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# ============================================================================

.PHONY: help
help: ## Help: Show this help message
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'


.PHONY: bump-ver-patch
bump-ver-patch: ## Helper: Bump version - patch level
	bumpversion patch


.PHONY: validate
validate: ## Validate: Run ansible-lint validator
	@echo ""
	@echo "== Run ansible-lint =="
	ansible-lint tower-*.yml


.PHONY: validate-all
validate-all: ## Validate: Run all validation scripts
validate-all: galaxy_install validate galaxy_remove


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


.PHONY: clean
clean: ## Clean: Clean all temporary files
	$(MAKE) -C docs clean
	rm -fr *~

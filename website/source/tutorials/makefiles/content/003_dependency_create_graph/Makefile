# ============================================================================
# Based on page:
#   https://gist.github.com/prwhite/8168133
# 
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# ============================================================================

.DEFAULT_GOAL = run-all-targets

.PHONY: help
help: ## Help: Show this help message
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

run-all-targets: ## Build: Run all targets (default)
run-all-targets: final-static-page graph-current-makefile

# == Build graph start - marker for doc ==
graph-current-makefile: ## Build: Create a graph of the current Makefile
graph-current-makefile:
	@make -Bnd final-static-page | make2graph | dot -Tpng -o Makefile_result_graph.png
# == Build graph stop - marker for doc ==

# NOTE: Following targets are not having description by purpose - goal of this file is to show resolving dependencies
# == Steps start - marker for doc ==
final-static-page: ## Build: Create and display a static page
final-static-page: static_page_display

nginx_install:
	@echo "STEP: Install Nginx"

nginx_run: nginx_install
	@echo "STEP: Run Nginx"

static_page_upload: static_page_create
	@echo "STEP: Upload static page to Nginx"

static_page_create:
	@echo "STEP: Create stacic Page"

static_page_display: static_page_upload nginx_run
	@echo "STEP: Display page"
# == Steps stop - marker for doc ==

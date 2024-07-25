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

# Original list of folders
FOLDERS := $(wildcard content/???_*)

# Folders to exclude
EXCLUDE_FOLDERS := \
	content/000_working_with_code \
	content/004_makefile_sdm

# Adjusted list of folders, excluding the specified ones
FOLDERS := $(filter-out $(EXCLUDE_FOLDERS),$(FOLDERS))

# Target to display the list of folders
list-folders: ## Debug: List of folders
	@echo "$(FOLDERS)" | tr ' ' '\n' | sort

# Default target to generate all Makefile_result.txt files
generate-all: ## Build: Generate all Makefile_result.txt files in content folders
generate-all: $(FOLDERS)

# Rule to run the Makefile in each folder and generate Makefile_result.txt
.PHONY: $(FOLDERS)
$(FOLDERS):
	$(MAKE) -C $@ -f Makefile | tail -n +2 | head -n -1 > $@/Makefile_result.txt

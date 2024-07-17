# ============================================================================
# Simple example of power from Makefile.
#
# Create list of steps which should be run (in valid order based
# dependencies).
#
# First step is target to achieve - then others tasks are based on
# dependencies.
# ============================================================================

conf_sec_page: conf_dns conf_web_srv conf_web_ssl
	@echo "STEP: Configure Secure Page"

conf_dns: have_srv inst_bind
	@echo "STEP: Configure DNS zones"

have_srv:
	@echo "STEP: Setup server"

inst_bind:
	@echo "STEP: Install and start BIND"

conf_web_srv: inst_nginx
	@echo "STEP: Configure page in WEB server"

inst_nginx: have_srv
	@echo "STEP: Install and start NGINX"

conf_web_ssl: data_csr conf_web_srv
	@echo "STEP: Configure CSR details (auto by LetsEncrypt)"

data_csr: inst_nginx
	@echo "STEP: Use LestEncrypt"

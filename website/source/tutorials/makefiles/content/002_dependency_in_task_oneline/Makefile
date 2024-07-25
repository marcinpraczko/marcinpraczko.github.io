# ============================================================================
# Simple example of power from Makefile.
#
# Makefile can be written as one liners - easier to parse and proceed
# ============================================================================

# == Steps with dependencies ==
conf_sec_page_deps := conf_dns
conf_sec_page_deps += conf_web_srv
conf_sec_page_deps += conf_web_ssl
conf_sec_page: $(conf_sec_page_deps); @echo "STEP: Configure Secure Page"

conf_dns_deps := have_srv 
conf_dns_deps += inst_bind
conf_dns: $(conf_dns_deps); @echo "STEP: Configure DNS zones"

conf_web_srv_deps := inst_nginx
conf_web_srv: $(conf_web_srv_deps); @echo "STEP: Configure page in WEB server"

conf_web_ssl_deps := data_csr
conf_web_ssl_deps += conf_web_srv
conf_web_ssl: $(conf_web_ssl_deps); @echo "STEP: Configure CSR details (auto by LetsEncrypt)"

inst_nginx_deps := have_srv
inst_nginx: $(inst_nginx_deps); @echo "STEP: Install and start NGINX"

data_csr_deps := inst_nginx
data_csr: $(data_csr_deps); @echo "STEP: Use LestEncrypt"

# == Steps without dependencies ==
have_srv:; @echo "STEP: Setup server"
inst_bind:; @echo "STEP: Install and start BIND"

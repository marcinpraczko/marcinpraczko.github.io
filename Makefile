sync-website-to-doc-folder:
	rsync -av --delete \
		--filter='P .nojekyll' \
		--filter='P CNAME' \
		website/build/html/ docs/

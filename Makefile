sync-website-to-doc-folder:
	rsync -av --delete \
		--exclude='__pycache__' \
		--exclude='to_review' \
		--exclude='.doctrees' \
		website/source/ docs/

sync-website-to-doc-folder:
	rsync -av --delete --filter='P .nojekyll' website/build/html/ docs/

Marcin Praczko main website
===========================

This project hosts my personal website, built with Sphinx and ablog.

Install
-------

- Install Python 3 and venv
- Create and activate a virtual environment (optional but recommended)
- Install dependencies:

  .. code-block:: bash

      pip install --upgrade pip
      pip install -r requirements.txt

Development
-----------

The project uses a ``Makefile`` to automate common tasks:

- **Update pip and dependencies:**

  .. code-block:: bash

      make pip-update-all

- **Update only requirements.txt:**

  .. code-block:: bash

      make pip-update-requirements

- **Install linters (flake8, pytest):**

  .. code-block:: bash

      make pip-install-linters

- **Run code validation (flake8 lint checks):**

  .. code-block:: bash

      make run-validation

- **Create a new blog post (interactive):**

  .. code-block:: bash

      make create-new-post

- **Sync built website to docs folder:**

  .. code-block:: bash

      make sync-website-to-doc-folder

Publishing
----------

Publishing to GitHub Pages is automated via GitHub Actions.
See [.github/workflows/gh-pages.yml](.github/workflows/gh-pages.yml) for details.

- On every push to any branch (affecting `website/source/**`), the workflow:
  - Installs dependencies and linters using Makefile targets
  - Runs code validation
  - Builds the documentation (`make -C website html`)
  - Uploads the generated site to GitHub Pages (on `main` branch)

Resources
---------

Following pages helped me to create this website:

- https://www.sphinx-doc.org/en/master/usage/installation.html
- https://ablog.readthedocs.io/en/stable/
- https://sublime-and-sphinx-guide.readthedocs.io/en/latest/images.html
- https://www.errbufferoverfl.me/posts/2020/sphinx-blog-part-one/
- https://python.plainenglish.io/building-a-personal-blog-with-python-and-sphinx-45f9794869a4

I've mixed between last two - however probably last is the one which I like.


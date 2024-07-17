# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Marcin Prączko website'
copyright = '2024, Marcin Prączko'
author = 'Marcin Prączko'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx_panels",
    "sphinx_tabs.tabs",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

# -- PyData theme and ABLOG --
post_auto_image = 1

html_theme_options = {
   "navigation_with_keys": False,
   "navbar_align": "right",
    "logo": {
        "text": "Marcin Prączko Website",
    }
}

html_sidebars = {
    # Custom layout for blog
   'blog/*': ['ablog/postcard.html', 'ablog/recentposts.html',
               'ablog/tagcloud.html', 'ablog/categories.html',
               'ablog/archives.html', ],
   'posts/*': ['ablog/postcard.html', 'ablog/recentposts.html',
               'ablog/tagcloud.html', 'ablog/categories.html',
               'ablog/archives.html', ],
}

# -- TODO --
# Display todos by setting to True
todo_include_todos = True
todo_emit_warnings = True
todo_link_only = True

# Exclude folders
exclude_patterns = ['to_review']

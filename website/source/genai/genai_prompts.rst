TOSORT - following prompts
==========================

Following prompts could be used for creating a starting project for a simple app for Sphinx.

.. todo:: This is not a complete list of prompts, but it should provide a good starting point for further exploration.


Initial Project Setup Prompt
----------------------------

**Prompt:**

    Please scaffold a project for documenting and visualizing Graphviz DOT diagrams with Sphinx.

    The project should include:

    - A Makefile that automates DOT -> SVG conversion and Sphinx documentation build.
    - Sphinx documentation with a modern theme (suggest one).
    - Shell scripts for generating SVGs and RST files dynamically from DOT files.
    - A sample README.md with usage instructions.
    - Place DOT and SVG files in a suitable subfolder (e.g., _images).
    - Ensure the workflow is automated: adding/removing DOT files updates SVGs and documentation.
    - Add a .gitignore for build and generated files.
    - Make it cross-platform if possible, but Linux/WSL/Bash is fine as default.


README.md Python Environment Prompt
-----------------------------------

**Prompt:**

    Please generate a concise README.md section for Python environment setup using uv.

    Include commands for creating a virtual environment, installing dependencies from requirements.txt, and freezing/updating requirements.
    Mention that the automation scripts are Bash-based and recommend WSL or Git Bash for Windows users.


Workspace Review Prompt
-----------------------

**Prompt:**

    Please review my current project workspace for a Sphinx-based documentation and diagram automation project.

    List any missing or redundant files.
    Suggest improvements for automation, file organization, and cross-platform compatibility.
    Check if all scripts are referenced in the Makefile and if static assets are in the correct place.
    Recommend .gitignore entries and any README improvements.
    Summarize your findings in a table.

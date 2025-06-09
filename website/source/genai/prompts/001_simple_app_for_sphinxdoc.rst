001 - Simple App for Sphinx Documentation
=========================================

.. contents:: Table of Contents
   :local:
   :depth: 2


Overview
--------

This document provides prompts for creating a simple app that integrates with Sphinx documentation to visualize Graphviz ``DOT`` diagrams.
The app will automate the conversion of ``DOT`` files to ``SVG`` format and generate corresponding ``Sphinx`` documentation.


Story behind following prompts
------------------------------

One day I needed to document a project that involved complex Graphviz ``DOT`` diagrams. I wanted to visualize these diagrams in ``Sphinx`` documentation. 
I decided to automate the workflow using a combination of ``Makefile``, ``shell scripts``, and ``Sphinx-doc``. 
The goal was to create a seamless experience where adding or removing ``DOT`` files would automatically update the ``SVGs`` and documentation.

Of course I used `GitHub Copilot`_ to help me with the code snippets. Once final project did work I created a set of prompts to help others replicate the process easily.


Prompts
-------

+----------------------+----------------------+
| Field                | Value                |
+======================+======================+
| Date                 | ``2025/06``          |
+----------------------+----------------------+
| Version              | ``0.1.0``            |
+----------------------+----------------------+
| Tested with          | `GitHub Copilot`_    |
+----------------------+----------------------+
| Model                | ``GPT-4.1``          |
+----------------------+----------------------+

Prompt 1: Initial Project Setup
+++++++++++++++++++++++++++++++

**Prompt:**

    Please scaffold a project for documenting and visualizing Graphviz ``DOT`` diagrams with ``Sphinx``.

    The project should include:

    - A ``Makefile`` that automates ``DOT -> SVG`` conversion and ``Sphinx`` documentation build.
    - ``Sphinx`` documentation with a modern theme (suggest one).
    - Shell scripts for generating ``SVGs`` and ``RST`` files dynamically from ``DOT`` files.
    - A sample ``README.md`` with usage instructions.
    - Place ``DOT`` and ``SVG`` files in a suitable subfolder (e.g., ``_images``).
    - Ensure the workflow is automated: adding/removing ``DOT`` files updates ``SVGs`` and documentation.
    - Add a ``.gitignore`` for build and generated files.
    - Make it cross-platform if possible, but ``Linux/WSL/Bash`` is fine as default.


Prompt 2: Create README.md for Python Environment
+++++++++++++++++++++++++++++++++++++++++++++++++

**Prompt:**

    Please generate a concise ``README.md`` section for Python environment setup using ``uv`` tool.

    - Include commands for creating a virtual environment, installing dependencies from ``requirements.txt``, 
      and freezing/updating requirements.
    - Mention that the automation scripts are ``Bash``-based and recommend ``WSL`` or ``Git Bash`` for Windows users.


Prompt 3: Final Workspace Review
++++++++++++++++++++++++++++++++

**Prompt:**

    Please review my current project workspace for a ``Sphinx``-based documentation and diagram automation project.

    - List any missing or redundant files.
    - Suggest improvements for automation, file organization, and cross-platform compatibility.
    - Check if all scripts are referenced in the ``Makefile`` and if static assets are in the correct place.
    - Recommend ``.gitignore`` entries and any ``README`` improvements.
    - Summarize your findings in a table.


References
----------

.. _DOT: https://graphviz.org/doc/info/lang.html
.. _GitHub Copilot: https://github.com/features/copilot
.. _make: https://www.gnu.org/software/make/
.. _OpenAI Model GPT-4.1: https://openai.com/index/gpt-4-1/
.. _OpenAI Models: https://platform.openai.com/docs/models
.. _SVG: https://developer.mozilla.org/docs/Web/SVG

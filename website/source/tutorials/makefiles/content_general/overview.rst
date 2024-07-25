Overview
========

.. meta::
    :tutorial_version: 1.0
    :creator: Marcin Prączko

This tutorial will help you understand how to create a simple ``Makefile`` and how to use it to automate tasks.

Tutorial Information
--------------------

.. list-table::
   :widths: 25 75

   * - Tutorial Version
     - 1.0
   * - Creator
     - Marcin Prączko

Introduction
------------

In general, a ``Makefile`` is a file that contains a set of rules used to build software.
It is used to automate the process of building software, however, it can also be used for other purposes as outlined below:

- Running different tasks (not only building software)
- Creating a clear dependency of tasks to help understand how tasks should be run in order
- Self-documented Makefile to help understand what tasks are available
- One-liners in Makefile

Runinng Makefile
----------------

During work with ``Makefile``, it is important to know what tasks are available.
This is important as many projecs run default task when ``make`` is run without any arguments.
And this can be dangerous if default task is not what you expect.

.. important::

  - In all examples in this tutorials one can run ``make`` without any arguments (safe to run)
  - In some examples running ``make`` without any arguments will display help
  - This is designed in this tutorial - however please be careful when running ``make`` without any arguments in others projects

Display help
++++++++++++

.. code-block:: bash

    make
    ...
    # Help will be displayed here

- In all cases running ``make`` will automatically run default task.
- In this tutorial, default task for many Makefiles is to display help.

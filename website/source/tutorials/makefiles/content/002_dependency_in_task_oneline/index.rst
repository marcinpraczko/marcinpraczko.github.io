.. _create_nice_dependency_of_tasks_one_liners:

Create nice dependency of tasks - one liners
============================================

In previous example (:ref:`create_nice_dependency_of_tasks`) we have shown how to create nice dependency of tasks in ``Makefile``.
However presented syntax can be not easy to read for some people and when dependencies will grow, it will be hard to maintain.

In this example we will show how to create one liners in Makefile and how to create dependencies which are easier to read.

Example scenario
----------------

Lets reuse scenario from previous :ref:`create_nice_dependency_of_tasks_scenario`.

Code
----

Following example shows example of one liners in Makefile.
By meaning ``one liners`` we are saying that we are defining dependencies and task in one line.
However definition of dependencies are separate lines easy to read.

**Code:**

.. literalinclude:: Makefile
   :language: make


Result
------

This section shows result when ``make`` is running without any arguments.

.. literalinclude:: Makefile_result.txt
   :language: console


Summary
-------

In this example we have shown how to create one liners in Makefile.
By using one liners we can create dependencies which are easier to read and maintain.

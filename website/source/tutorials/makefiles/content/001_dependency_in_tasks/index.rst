.. _create_nice_dependency_of_tasks:

Create nice dependency of tasks
===============================

Imagine that you need to work on complex task which has many dependencies in actions.
And you would like to know what to work on first and what to work on next.

It is important to have a way how to detect dependencies and how to run only tasks which are necessary.

.. _create_nice_dependency_of_tasks_scenario:

Example scenario
----------------

Expected scenario is following:

- You need to setup web server with proper domain and SSL certificate.
- You know required steps (based on you past experience).
- You are owning all infrastructure components - so you can do whatever you want.
- You may not know all dependencies in actions - this can be added during work.

Now you can use Makefile to help you to know order of actions which are required.

- This is possible by defining dependencies in Makefile (``Make`` is doing great job for detecting dependencies).
- This can be first step for automation - which can be added later.

Code
----

Following example shows power of Makefile for detecting dependencies.

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

Result section above shows that Makefile is able to detect dependencies in actions and present them in order which one
should follow to finish task mentioned in ``Example scenario``.

In short:

- To setup secure page, one need to first

  - setup web server
  - create domain
  - create SSL certificate

This is very powerful feature of Makefile which can be used in many scenarios.

Self documented Makefile - Simple example
=========================================

Following example shows simple self documented ``Makefile``

- Each target is display with description in single line
- Character ``:`` is used to separate target name and description

.. hint::

   - One can use multiple ``:`` to separate details in description (different fields)
   - Following example uses command ``column`` to display tasks in nice format

.. important::

   - If one uses multiple ``:`` characters, one should update each description to have the same numbers of ``:``.

Code
----

.. literalinclude:: Makefile
   :language: make

Result
------

Running ``make`` without any arguments will display list of available tasks.

.. literalinclude:: Makefile_result.txt
   :language: console

Im result above one can see three columns:

- First is with name of target
- Second is with group for target
- Last is longer description

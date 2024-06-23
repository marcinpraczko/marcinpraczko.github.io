Emacs Fuzzy searching in buffer
===============================

.. post:: Apr 16, 2024
   :tags: emacs, search, buffer
   :category: Editors
   :author: Marcin Prączko
   :language: en


Introduction
------------

Fuzzy searching is a powerful feature that allows you to search for text in a buffer

Configuration
-------------

To enable fuzzy searching in Emacs, you need to install the ``ivy`` and ``swiper`` package.
You can do this by running the following commands from emacs:

.. code-block:: text

    M-x package-install RET ivy RET
    M-x package-install RET swiper RET

Please also add the following configuration to your ``init.el`` file:

.. code-block:: lisp

    (ivy-mode)
    (require 'swiper)
    (global-set-key (kbd "C-s") 'swiper)

Reload your configuration by running ``M-x eval-buffer``.

After you've added the configuration, you can use the ``C-s`` keybinding to start a fuzzy search in the current buffer.


Screenshot
----------

Following screenshot shows the fuzzy search in action:

.. image:: _static/img/002-1.jpeg
  :width: 512
  :alt: 002-1.jpeg

In the displayed screenshot, the word ``Task`` is searched for in the buffer. Notice how the search results are highlighted in the buffer.

- After pressing ``C-s``, the search prompt appears at the bottom of the buffer.
- As you type, the search results are updated in real-time.
- Arrows presnets

1. Searching text
2. All items found in buffer
3. All recurence of the word has been selected

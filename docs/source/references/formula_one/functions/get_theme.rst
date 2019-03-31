Get theme
=========

``getTheme()`` is at the heart of ``Omniport`` themes. It returns the current
theme colour out of available Semantic colours.

Signature
---------

.. code-block:: javascript

    function getTheme() {
        ...
        return theme
    }

Return
------

:Type:
    ``string``
:Data:
    - can be passed directly to ``Semantic UI`` components
    - returns currently active theme colour as ``string``
    - returns ``'blue'`` if no colour is set and also sets theme colour to 
      ``'blue'``
    - **Enums:**  ``red``, ``orange``, ``yellow``, ``olive``, ``green``, 
      ``teal``, ``blue``, ``violet``, ``purple``, ``pink``, ``black``

Examples
--------

.. code-block:: javascript

    import { getTheme } from 'formula_one'

Importing ``getTheme()`` from ``formula_one``

.. code-block:: javascript

    > getTheme()
    'orange'
    
Using ``getTheme()`` to get currently selected theme

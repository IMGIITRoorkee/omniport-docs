Get theme object
================

``getThemeObject()`` is the function that returns colour description object of
currently selected theme.

Signature
---------

.. code-block:: javascript

    function getThemeObject() {
        ...
        return themeObject
    }

Return
------

:Type:
    ``{object}``
    
    .. code-block:: javascript

        {
            name: {string},
            verboseName: {string},
            description: {string},
            hexCode: {string}
        }


:Data:
    - returns an object describing active theme colour
    - returns the object corresponding to the colour ``'blue'`` if no colour is
      set and also sets theme colour to ``'blue'``
    - can be used when active theme is to be passed to JSX elements' ``style``

Examples
--------

.. code-block:: javascript

    import { getThemeObject } from 'formula_one'

Importing ``getThemeObject()`` from ``formula_one``

.. code-block:: javascript

    > getThemeObject()
    {
        name: "orange",
        verboseName: "Maverick Orange",
        description: "Unorthodox and chaotic",
        hexCode: "#f2711c"
    }

Using ``getThemeObject()`` to get current selected theme object

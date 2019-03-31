Get cookie
==========

``getCookie()`` is a function which makes consuming cookies *a piece of cake*.
It returns the value of the cookie corresponding to name passed to it as
parameter ``cname``.

Signature
---------

.. code-block:: javascript

    function getCookie(cname) {
        ...
        return value
    }

Parameters
----------

#. ``cname``

    :Type:
        ``string``
    :Default:
        **\*required**
    :Description:
        the name of the cookie whose value is being retrieved

Return
------

:Type:
    ``string``
:Data:
    - value of the cookie whose name is ``cname``
    - ``null`` if the specified cookie is not found

Examples
--------

.. code-block:: javascript

    import { getCookie } from 'formula_one'

Importing ``getCookie()`` from ``formula_one``.

.. code-block:: javascript

    > getCookie('csrftoken')
    '4OgZaiZcwEHAAeqnzqrn2jFubHe7IemgS07ZJJ0CltuQD3e0MSHIKaAtqeBb7HhD'

Using ``getCookie()`` to read the cookie named 'csrftoken'.
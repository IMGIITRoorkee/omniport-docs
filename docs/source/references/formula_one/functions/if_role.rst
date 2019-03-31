If role
=======

``ifRole()`` is a function which returns the status of a role corresponding to a
passed array of a user's roles.

Signature
---------

.. code-block:: javascript

    function ifRole(roles, role) {
        ...
        return status
    }

Parameters
----------

#. ``roles``

    :Type:
        ``[object]``
    :Default:
        **\*required**
    :Description:
        the array of **role objects** obtained by requesting ``who_am_i/``

        .. code-block:: json

            [
                {
                    "role": "Student",
                    "activeStatus": "ActiveStatus.IS_ACTIVE"
                },
                {
                    "role": "Maintainer",
                    "activeStatus": "ActiveStatus.IS_ACTIVE"
                }
            ]

#. ``role``

    :Type:
        ``string``
    :Default:
        **\*required**
    :Description:
        the role whose existence is being checked
        
Return
------

:Type:
    ``enum`` (``string``)
:Data:
    - ``NOT_ROLE`` if required role is not matched with any role in the array.
    - **Enums:** ``IS_ACTIVE``, ``HAS_BEEN_ACTIVE``, ``WILL_BE_ACTIVE``, 
      ``NOT_ROLE``

Examples
--------

.. code-block:: javascript

    import { ifRole } from 'formula_one'

Importing ``ifRole()`` from ``formula_one``

.. code-block:: javascript

    > const roles = [
                {
                    "role": "Student",
                    "activeStatus": "ActiveStatus.IS_ACTIVE"
                },
                {
                    "role": "Maintainer",
                    "activeStatus": "ActiveStatus.IS_ACTIVE"
                }
            ]

    > ifRole(roles, 'Maintainer')
    'IS_ACTIVE'

    > ifRole(roles, 'Faculty')
    'NOT_ROLE'

Using ``ifRole()`` to get the status of various role of a person
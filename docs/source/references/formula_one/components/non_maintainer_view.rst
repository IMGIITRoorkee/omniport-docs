Non-maintainer view
===================

``<NonMaintainerView>`` is a component that wraps components which are
strictly useless for maintainers if they have certain permissions.

Props
-----

#. ``which``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the permission that the user, who must not be a maintainer, or is
        supposed not to have

Example usage
-------------

.. code-block:: javascript

  import { NonMaintainerView } from 'formula_one'

Importing ``NonMaintainerView`` from ``formula_one``

.. code-block:: jsx

  <NonMaintainerView which='helpcentre'>
    ...
  </NonMaintainerView>

Using ``NonMaintainerView`` passing prop ``which``

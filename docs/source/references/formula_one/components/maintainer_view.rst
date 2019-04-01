Maintainer view
===============

``MaintainerView`` is a component that wraps components which are meant to be
viewed only by maintainers with special permissions.

Props
-----

#. ``which``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the permission that the user, who must be a maintainer, is supposed to
        have

Example usage
-------------

.. code-block:: javascript

  import { MaintainerView } from 'formula_one'

Importing ``MaintainerView`` from ``formula_one``

.. code-block:: jsx

  <MaintainerView which='helpcentre'>
    ...
  </MaintainerView>

Using ``MaintainerView``, passing prop ``which``

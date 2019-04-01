Tile card
==========

A *tile card* is a component that shows information about one unit of many
similar units in an organised way, in an aesthetic card.

Props
-----

#. ``name``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the heading to be used in the card

#. ``desc``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the description that is shown below the heading

#. ``imageUrl``

    :Type:
      ``string``
    :Default:
      ``iconName``, see below
    :Description:
      | the associated image to be display in the card

#. ``iconName``

    :Type:
      ``enum (string)``
    :Default:
      ``group``
    :Description:
      | the icon to display in case an image URL is not passed in the props
      | **Enums**: For a comprehensive collection of valid inputs, refer to the 
        `icon list <https://react.semantic-ui.com/elements/icon/>`_.

Example usage
-------------

.. code-block:: javascript

  import { TileCard } from 'formula_one'

Importing ``TileCard`` from ``formula_one``

.. code-block:: jsx
    
  <TileCard
    name='Alohomora'
    desc='Reset passwords, no-questions asked'
    imageUrl='/path/to/image.jpg'
    iconName='cube'
  />

Using ``TileCard``, passing all the props

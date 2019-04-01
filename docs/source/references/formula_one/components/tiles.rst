Tiles
=====

Tiles are grids of tile cards.

Props
-----

#. ``tiles``

    :Type:        
      ::
        
        [{
          name: string,
          desc: string,
          iconName: string,
          imageUrl: string,
          link: link
        }]

    :Default:
      **\*required**
    :Description:
      Refer to the props for :doc:`the tile card component <tile_card>`, except
      for ``link``. 
      
      :link:
        Defines URL to which corresponding ``TileCard`` should point.

Example usage
-------------

.. code-block:: javascript

  import { Tiles } from 'formula_one'

Importing ``Tiles`` from ``formula_one``

.. code-block:: javascript

  const tiles = [{
    name: 'Alohomora',
    desc: 'Reset passwords, no-questions asked',
    imageUrl: '/path/to/image.jpg',
    iconName: 'cube',
    link: '/alohomora'
  }]

Defining an array of objects to pass in ``tiles``

.. code-block:: jsx
    
  <Tiles
    tiles={tiles}
  />

Using ``Tiles``, passing all the props

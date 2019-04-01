App footer
==========

The *app footer* is always attached to the bottom of the screen and shows 
copyright and maintainer information. The footer is also some the coolest code
in the entirety of Omniport's frontend.

Props
-----

#. ``creators``

    :Type:
      ::
          
        [{
          name: string,
          role: string,
          <link: string>
        }]
      
      <> denotes optional field

    :Default:
      **\*required**
    :Description:
      | the creators who deserve credit for their app in the footer

Example usage
-------------

.. code-block:: javascript

  import { AppFooter } from 'formula_one'

Importing ``AppFooter`` from ``formula_one``

.. code-block:: javascript
    
  const creators = [
    {
      name: 'Dhruv Bhanushali',
      role: 'Backend developer',
      link: 'https://dhruvkb.github.io/'
    },
    {
      name: 'Praduman Goyal',
      role: 'Frontend developer',
      link: 'https://pradumangoyal.github.io/'
    }
  ]

Defining an array of objects to pass in ``creators``

.. code-block:: jsx

  <AppFooter creators={creators} />

Using ``AppFooter``, passing creators list

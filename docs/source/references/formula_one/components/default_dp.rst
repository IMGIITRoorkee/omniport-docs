Default DP
==========

The *default DP* component displays the first letter of the prop ``name`` in the
shape of circle with the theme colour as background. It can be used whenever
display image is not provided by user. 

Props
-----

#. ``name``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the string whose first letter will be shown in the component

#. ``size``

    :Type:
      ``string``
    :Default:
      ``'1.5em'``
    :Description:
      | the ``font-size`` property of the letter

Example usage
-------------

.. code-block:: javascript

  import { DefaultDP } from 'formula_one'

Importing ``DefaultDP`` from ``formula_one``

.. code-block:: jsx

  <DefaultDP name='Praduman Goyal' size='3em' />

Using ``DefaultDP`` passing name and size

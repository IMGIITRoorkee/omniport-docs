No match
========

The ``<NoMatch>`` component is a very beautiful full page 404 component with its
own header and footer and is mobile responsive.

Props
-----

There are absolutely none!

Example usage
-------------

.. code-block:: javascript

  import { NoMatch } from 'formula_one'

Importing ``NoMatch`` from ``formula_one``

.. code-block:: jsx

  <Route component={NoMatch} />

Using ``NoMatch`` in main routes

.. code-block:: jsx
 
  <Redirect to='/404' />

An app can redirect to main 404 when there is no path route matched. 

.. note:: 

  The standard way to use it is to redirect to it. Using it within one's header
  and footer can unleash a world of ugly and nasty.

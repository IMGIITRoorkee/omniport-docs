App main
========

``<AppMain>`` is a wrapper around the container in between your ``<AppHeader>`` 
and ``<AppFooter>`` which applies some default style to the app.

Example usage
-------------

.. code-block:: javascript

  import { AppMain } from 'formula_one'
  
  import style from '../css/app.css'

Importing ``AppMain`` from ``formula_one``

.. code-block:: jsx

  <AppHeader {...props} />

  <div styleName='style.app-container'>
    <AppMain>
        ...
    </AppMain>
  </div>

  <AppFooter {...props} />

Using ``AppMain`` in an app

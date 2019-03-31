Common apps
===========

``commonApps()`` is a function which returns the list of apps obtained by the
intersection of two lists, one being the API list obtained by requesting on
``apps/app/`` and one being set in ``config.json`` at frontend.

Signature
---------

.. code-block:: javascript

  function commonApps(apiList) {
    ...
    return commonList
  }

Parameters
----------

#. ``apiList``

  :Type:
    ``[object]``
  :Default:
    **required**
  :Description:
    the array of **app objects** obtained by requesting ``apps/app/``

    .. code-block:: json

      [
        {
          "nomenclature": {
            "name": "one",
            "verboseName": "One"
          },
          "baseUrls": {
            "http": "one/",
            "ws": null,
            "static": "one/"
          },
          "assets": {
            "favicon": "assets/favicon.ico",
            "icon": null,
            "logo": "assets/logo.svg"
          },
          "description": "App number one"
        },
        {
          "nomenclature": {
            "name": "two",
            "verboseName": "Two"
          },
          "baseUrls": {
            "http": "two/",
            "ws": null,
            "static": "two/"
          },
          "assets": {
            "favicon": "assets/favicon.ico",
            "icon": "assets/icon.svg",
            "logo": "assets/logo.svg"
          },
          "description": "App number two"
        }
      ]
        
Return
------

  :Type:
    ``[object]``
  :Data:
    intersection of the two list with the object in the following form

    .. code-block:: json

      {
        "assets": {
          "favicon": "assets/favicon.ico",
          "icon": "assets/icon.svg",
          "logo": "assets/logo.svg"
        },
        "baseUrl": "/one",
        "baseUrls": {
          "http": "one/",
          "ws": null,
          "static": "one/"
        },
        "description": "App number one",
        "nomenclature": {
          "name": "one",
          "verboseName": "One"
        },
        "source": "one/src/index"
      }

Examples
--------

  .. code-block:: javascript

    import { commonApps } from 'formula_one'

  Importing ``commonApps()`` from ``formula_one``

  .. code-block:: javascript

    commonApps(apiList)
      
  Using ``commonApps()``, returns an array of object of type described above
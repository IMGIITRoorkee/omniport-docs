App details
===========

``appDetails()`` is a function which returns the config object stored at the
frontend of the requested app according to their ``appName`` (**not**
``appDisplayName``) which is generally of the form ``placement_and_internship``.

Signature
---------

.. code-block:: javascript

  function appDetails('placement_and_internship') {
    ...
    return {
      present: {bool},
      details: {object}
    }
  }

Parameters
----------

#. ``appName``

  :Type:
    ``string``
  :Default:
    **\*required**
  :Description:
    the app whose config object is required (**not** ``appDisplayName``)
Return
------

  :Type:
    ``{object}``
  :Data:
    Object containing ``present`` and ``details``
    
    :present:
      ``bool`` that specifies whether the app exists
    :details:
      App config object defined in ``config.json`` of the app
    
Examples
--------

.. code-block:: javascript

  import { appDetails } from 'formula_one'

Importing ``appDetails()`` from ``formula_one``

.. code-block:: javascript

  > appDetails('placement_and_internship')
  {
    present: true,
    details: {
      nomenclature: {
        name: "placement_and_internship",
        verboseName: "Placement and Internship"
      },
      baseUrl: "/placement_and_internship",
      source: "placement_and_internship/src/index"
    }
  }
    
Using ``appDetails()`` to get config of an app named
``placement_and_internship``
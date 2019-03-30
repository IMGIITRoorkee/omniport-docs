``config.json`` on the frontend
===============================

Purposes
--------

``config.json`` is one important pillar of Omniport's plug-and-play architecture.
It primarily serves the following three purposes. 

These configuration files are used to generate ``omniport\core\configs.json``
and ``omniport\core\primarySidebarConfigs.json`` which can be used in your apps.

Nomenclature
++++++++++++

The nomenclature part of the config file is used to define the internal and 
display name of the app, which in turn, defines app nomenclature all around the
code. It requires the ``nomenclature`` key to be defined in ``config.json``.

:nomenclature:
  | Nomenclature related fields of an app.
  | ``{object}`` which has the following subkeys

  :name: 
    | The name that is used internally to refer to an app.
    | ``string``

  :verboseName:
    | The display name of the app with spaces and proper punctuation.
    | ``string``

Dynamic routes
++++++++++++++

``omniport/core/configs.json`` created during build using ``discovery.js`` is
used to create dynamic ``Route`` component which act as an entry point in 
Omniport for the service or app. It requires two keys in config i.e. ``baseUrl``
and ``source``.

:baseUrl:
  | The URL on which app has to be rendered.
  | ``string``
:source:
  | The source to the ``index.js`` file of the app relative to the ``omniport``
    directory.
  | ``string``
   
Sidebar configuration
+++++++++++++++++++++

.. note::

  This section only applies to services.

``discovery.js`` also creates ``omniport/core/primarySidebarConfigs.json`` using
config files in sub-folders of services. This ``primarySidebarConfigs.json``, as
the name suggests is used to create the sidebar the appears in Omniport core.
This functionality allows Omniport to pin some of services to the sidebar at a
position determined by its priority.

:primarySidebar:
  | primarySidebar related fields of a service.
  | ``{object}`` which has the following subkeys.

  :icon: 
    | The name of the icon from the collection provided by
      `Semantic UI <https://react.semantic-ui.com/elements/icon/>`_.
    | ``string``
  :priority:
    | Defines the placement of the button in the sidebar.
    | Services with higher priority appear higher in the sidebar.
    | If not provided, it is assumed ~infinite.
    | If two services have the same priority, they are sorted lexicographically.
    | ``integer``

Examples
--------

Service
+++++++

An example ``config.json`` for a service **having its button** in sidebar can be as 
follows.

.. code-block:: json

  {
    "nomenclature": {
      "name": "developer",
      "verboseName": "Developer"
    },
    "baseUrl": "/developer",
    "source": "developer/src/index",
    "primarySidebar": {
      "icon": "code",
      "priority": 6
    }
  }

-----

An example ``config.json`` for a service, which **doesn't require its button** 
in sidebar can be as follows.

.. code-block:: json

  {
    "nomenclature": {
      "name": "auth",
      "verboseName": "Auth"
    },
    "baseUrl": "/auth",
    "source": "auth/src/index"
  }

App
+++

An example ``config.json`` for an app can be as follows.

.. code-block:: json

  {
    "nomenclature": {
      "name": "placement_and_internship",
      "verboseName": "Placement and Internship"
    },
    "baseUrl": "/placement_and_internship",
    "source": "placement_and_internship/src/index"
  }

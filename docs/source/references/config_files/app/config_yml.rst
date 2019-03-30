``config.yml`` on the backend
=============================

Purposes
--------

``config.yml`` is the crux of Omniport's plug-and-play architecture. It 
primarily serves the following purposes.

These configurations are processed by the modules ``discovery`` and 
``configuration`` and their processed data can be accessed as follows.

.. code-block:: python

  from django.conf import settings

  DISCOVERY = settings.DISCOVERY
  
  ...  # Do something with DISCOVERY

This ``DISCOVERY`` object of ``class Discovery`` contains the fields
``service_configuration_map`` and ``app_configuration_map`` which can be used in
your apps.

Nomenclature
++++++++++++

The nomenclature part of the config file is used to define the internal and 
display name of the app, which in turn, defines the app nomenclature all around
the code. It requires the ``nomenclature`` key to be defined in ``config.yml``.

:nomenclature:
  | Nomenclature related fields of an app
  | ``{object}`` which has the following subkeys

  :name: 
    | The name that is used internally to refer to an app
    | ``string``

  :verboseName:
    | The display name of the app with spaces and proper punctuation
    | ``string``

Description
+++++++++++

This is the short app description that populates a number of places where the 
app description is shown such as on the ``apps/`` page of service ``apps``.

:description:
  | A brief description of the app
  | ``string``

Is API
++++++

This boolean field toggles whether the root URL of the app must be at ``/`` or
at ``/api/``. For all modern apps, this field must be set to ``true``.

Only legacy apps or special apps that need to run from the root URL path must 
set this field to false.

:isApi: 
  | Decides whether the app is an API or not
  | ``boolean`` set to ``true``

Acceptables
+++++++++++

.. note::

  This section only applies to apps.

The modules ``discovery`` and ``configuration`` while processing the config 
files also determine the various target demographics for any given app. The 
``acceptables`` key defines just that. The filters can be applied on the basis 
of user roles, their corresponding active statuses and the IP address of the 
request's origin.

This means that different users, having different roles, coming from different
IP address rings will be able to see different apps.

:acceptables:
  | The filters deciding the target demographic of an app
  | ``{object}`` which has the following subkeys

  :ipAddressRings:
    | The list of strings naming the IP address rings this app will serve
    | Should be a subset of ``ipAddressRings`` defined in ``base.yml``.
    | ``[string]``

  :roles:
    | The roles this app will serve
    | ``[{object}]`` where each has the following subkeys

    :name:
      | The name of any allowed role
      | Should be one of the roles defined in the ``kernel`` module.
      | ``string`` such as ``'Student'`` or ``'FacultyMember'``

    :activeStatuses:
      | The active statuses this app will serve
      | Should be one of the following.
      | ``IS_ACTIVE``
      | ``IS_INACTIVE``
      | ``HAS_BEEN_ACTIVE`` 
      | ``WILL_BE_ACTIVE``
      | ``[string]`` where each string is one of the above values.

Examples
--------

Service
+++++++

An example ``config.yml`` for a service can be as follows.

.. code-block:: yaml

  nomenclature:
    name: apps
    verboseName: Apps
  description: Find all the apps that make up Omniport
  baseUrls:
    http: apps/
  isApi: true

App
+++

An example ``config.yml`` for an app that allows active maintainers to reset 
people's passwords from within their workplace can be as follows.

.. code-block:: yaml

  nomenclature:
    name: alohomora
    verboseName: Alohomora
  description: Reset passwords, no-questions asked
  baseUrls:
    http: alohomora/
    static: alohomora/
  acceptables:
    ipAddressRings:
    - self
    - specifics
    - maintainers
    roles:
    - name: Maintainer
      activeStatuses:
      - IS_ACTIVE
  isApi: true

-----

An example ``config.yml`` targeting alumni, and alumnae, living anywhere in the 
world can be as follows.

.. code-block:: yaml

  nomenclature:
    name: alumni_connect
    verboseName: Alumni connect
  description: Talk to alumni and learn from their experience
  baseUrls:
    http: alumni_connect/
    static: alumni_connect/
  acceptables:
    roles:
    - name: Student
      activeStatuses:
      - HAS_BEEN_ACTIVE
  isApi: true


... access app registry?
========================

Discovery and Configuration allow Omniport to be extensible and tailored to the
needs and requirements of a particular institute. But this comes at the cost of
integrability as one app can never fully be sure of the existence of another.

Consider for example, the service Notifications, which delivers notifications
raised by apps. To decide whom it may deliver on behalf of, it needs to know,
dynamically, the list of apps that have been installed in the Omniport
ecosystem.

This is where accessing the app registry comes into the picture. This
functionality enables developers of services like Notifications, Feed and
Categories to be aware of the apps installed and configured by the sysadmin.

Fortunately Discovery provides this feature. To use it, first import the
function ``available_apps``.

.. code-block:: python
  
  from discovery.available import available_apps

Then in a function where the request object is available, such as a view or a
DRF viewset, invoke the ``available_apps`` function.
  
.. code-block:: python

  available_app_list = available_apps(request=request)

What you get back
-----------------

The return value is a list of pairs, not a list of names. Each pair holds the
directory the app was found in and the configuration parsed from its
``config.yml``, so unpack both and read what you need from the second.

.. code-block:: python

  for directory, configuration in available_apps(request=request):
      name = configuration.nomenclature.name
      verbose_name = configuration.nomenclature.verbose_name
      http_base = configuration.base_urls.http

The directory and the ``name`` are usually the same string, but they are two
different things and only the ``name`` is the one the rest of Omniport keys on.
Prefer it whenever you store or compare an app.

.. warning::

  ``available_apps`` reads ``request.ip_address_rings`` and ``request.roles``,
  which Omniport's middleware attaches on the way in. A request that has not
  been through that middleware carries neither, and the call fails with an
  ``AttributeError`` rather than returning an empty list. This rules out
  calling it from a Celery task or a management command, where there is no
  request at all. Work out the app list inside a view and pass it onward.

Narrowing the list
------------------

The function takes an optional second argument.

.. code-block:: python

  available_apps(request=request, search_term='placement_and_internship')

``search_term`` is compared for equality against the app's ``name``, so it
matches one app exactly or none. It is not a substring search and it is case
sensitive. Left out, it matches everything, which is why the plain call above
returns the whole list.

.. note::

  There is no equivalent for services. Every service is allowed for every user,
  so there is nothing to filter and no registry to consult. Read
  ``settings.DISCOVERY.services`` directly if you need them, or
  ``settings.DISCOVERY.get_app_configuration(name)`` to look up a single app or
  service by name.

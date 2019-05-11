... access app registry?
========================

Discovery and Configuration allow Omniport to be extensible and tailored to the
needs and requirements of a particular institute. But this comes at the cost of
integrability as one app can never fully be sure of the existence of another.

Consider for example, the service Helpcentre which allows users to ask queries
which may have to do with a particular app. To enable this functionality,
Helpcentre needs to know, dynamically, the list of apps that have been installed
in the Omniport ecosystem.

This is where accessing the app registry comes into the picture. This
functionality enables developers of services like Helpcentre and Notifications
to be aware of the apps installed and configured by the sysadmin.

Fortunately Discovery provides this feature. To use it, first import the
function ``available_apps``.

.. code-block:: python
  
  from discovery.available import available_apps

Then in a function where the request object is available, such as a view or a
DRF viewset, invoke the ``available_apps`` function.
  
.. code-block:: python

  available_app_list = available_apps(request=request)
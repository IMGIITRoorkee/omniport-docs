Start Django
============

.. note::

  This process requires the Django container to have been built beforehand. If 
  that is not the case, read :doc:`how to build the Omniport Django container
  <../docker/build/django>`.

This script starts a Django container with the code mounted in it making it easy
to deploy the development version of the app in a container and pre-configure it
to find the service containers and connect to them.

Usage
-----

.. code-block:: console

  [dev omniport-frontend]$ ./scripts/start/django.sh

Flags
-----

:-p:
  | The port to which the Django developer server must bind
  | ``number``

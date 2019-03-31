Start React
===========

.. note::

  This process requires the React container to have been built beforehand. If 
  that is not the case, read :doc:`how to build the Omniport React container
  <../docker/build/react>`.

This script starts a React container with the code mounted in it making it easy
to deploy the development version of the app in a container and pre-configure it
to find the API container and connect to it.

Usage
-----

.. code-block:: console

  [dev omniport-frontend]$ ./scripts/start/react.sh -d <DJANGO PORT>

Flags
-----

:-d:
  | The Django port where the API is up and running
  | ``number``, **required**

:-p:
  | The port to which the React developer server must bind
  | ``number``

Build frontend
==============

.. note::

  This process requires the React container to have been built beforehand. If 
  that is not the case, read :doc:`how to build the Omniport React container
  <../docker/build/react>`.

This scripts builds the production React app from the frontend codebase and places
the built files in a folder named ``build/``.

Usage
-----

.. code-block:: console

  [dev omniport-frontend]$ ./scripts/build/frontend.sh
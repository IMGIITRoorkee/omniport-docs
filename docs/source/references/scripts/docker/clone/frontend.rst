Frontend
========

``clone/frontend.sh`` sets up ``omniport-frontend`` inside the ``codebase/``
folder with the ``services`` required at the frontend.

.. warning::
  
  Running this script will remove any existing ``omniport-frontend/`` folder
  inside the ``codebase/`` directory.

Usage
-----

.. code-block:: console

  [apps omniport-docker]$ ./scripts/clone/frontend.sh

Working
-------

The script clones the repository ``omniport-frontend`` and then defers the
cloning process to the ``scripts/clone/everything.sh`` :doc:`script
<../../frontend/clone/everything>` in that repository.

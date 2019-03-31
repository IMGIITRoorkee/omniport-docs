Backend
=======

``clone/backend.sh`` sets up ``omniport-backend`` inside the ``codebase/``
folder with the ``services`` required at the backend.

.. warning::
  
  Running this script will remove any existing ``omniport-backend/`` folder
  inside the ``codebase/`` directory.

Usage
-----

.. code-block:: console

  [apps omniport-docker]$ ./scripts/clone/backend.sh

Working
-------

The script clones the repository ``omniport-backend`` and then defers the
cloning process to the ``scripts/clone/everything.sh`` :doc:`script
<../../backend/clone/everything>` in that repository.

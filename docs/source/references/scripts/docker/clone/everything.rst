Everything
==========

``clone/everything.sh`` aims to set up whole Omniport codebase in one command
with the basic services that Omniport expects to run smoothly on both the
frontend as well as the backend.

The script takes you through the steps of cloning the codebase.

.. warning::
  
  Running this script will remove any existing ``codebase/`` folder in the root
  directory.

Usage
-----

.. code-block:: console

  [apps omniport-docker]$ ./scripts/clone/everything.sh

Working
-------

Basically, all this script does is call two sub-scripts which in turn clone the
:doc:`backend <backend>` and :doc:`frontend <frontend>` codebases.

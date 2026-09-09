Memcached
=========

This script builds the Memcached container that acts as the cache for all Omniport apps and services.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/memcached.sh

Unlike most of the build scripts, this one asks you nothing.
It enters ``memcached/``, builds the image and tags it ``omniport-memcached:latest`` alongside a tag carrying the Unix timestamp of the build.
There is no environment file to recreate and no questionnaire to answer, so the script runs to completion on its own.

The image is the official Memcached image with ``netcat`` added, which is what the container uses to report its own health on port 11211.
Exactly one container runs it, the ``cache`` service, whose name is also the host name that the rest of the project reaches the cache by.

Remember to populate this host name and the port ``11211`` in the :doc:`Django project-level configuration file <../../../config_files/project/base_yml>`.

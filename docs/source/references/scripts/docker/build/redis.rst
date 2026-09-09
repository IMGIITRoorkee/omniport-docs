Redis
=====

This script builds the Redis container that backs the channel layer, the session store and the other key-value stores used across Omniport.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/redis.sh

Unlike most of the build scripts, this one asks you nothing.
It enters ``redis/``, builds the image and tags it ``omniport-redis:latest`` alongside a tag carrying the Unix timestamp of the build.
There is no environment file to recreate and no questionnaire to answer, so the script runs to completion on its own.

The image is the official Redis image with a health check script added, which reports the container healthy for as long as the server answers a ping.

One build is enough for five containers.
The Compose file starts ``channel-layer``, ``session-store``, ``communication-store``, ``verification-store`` and ``application-store`` from this single image, each with a volume of its own, so nothing one of them holds is visible to the others.

Remember to populate the name of each of these five containers, and the port ``6379``, in the :doc:`Django project-level configuration file <../../../config_files/project/base_yml>`.

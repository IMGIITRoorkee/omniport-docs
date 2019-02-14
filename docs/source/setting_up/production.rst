Production
==========

With everything set up, the flows diverge. This is how to deploy Omniport.

As ``apps``, enter ``omniport-docker/codebase/omniport-frontend``. Build the 
frontend for NGINX to serve.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/frontend.sh

This should build your React app and place it a folder for NGINX to serve.

Then just start all services using Docker Compose.

.. code-block:: console

  [apps omniport-docker]$ docker-compose up -d

You should be able to access your app on the domains you specified in NGINX,
provided you have the DNS routing properly set up.

To enter the container for any service, execute this command.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec <service_name> sh

.. note::

  Some services, namely those built off of Debian, have ``bash`` installed. Most
  don't. So the best way to go about it is to execute ``sh`` and once in the 
  container, execute ``bash``.

From time to time, you will have to enter the Django container to make and run
migrations, collect static files and do the occasional housekeeping.

Relax.
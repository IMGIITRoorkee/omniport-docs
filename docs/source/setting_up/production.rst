:sourcefiles:
  omniport-frontend/scripts/build/frontend.sh
  omniport-docker/docker-compose.yml

Production
==========

With everything set up, the flows diverge. This is how to deploy Omniport.

As ``apps``, enter ``omniport-docker/codebase/omniport-frontend``. Build the 
frontend for NGINX to serve.

.. code-block:: console

  [apps omniport-frontend]$ ./scripts/build/frontend.sh

This should build your React app and place it in a folder for NGINX to serve.
The script belongs to the frontend rather than to Omniport Docker, and it
builds inside the React image, so run it from this directory and only after
that image has been built.

Then just start all services using Docker Compose.

.. code-block:: console

  [apps omniport-docker]$ docker-compose up -d

You should be able to access your app on the domains you specified in NGINX,
provided you have the DNS routing properly set up.

.. warning::

  A first deployment is not finished here. Nothing migrates the database or
  collects static files for you, so until you have done both by hand the portal
  answers with errors on every page that reads a model and with 404 on every
  stylesheet, script and image it tries to load. Do both now, in the intranet
  or Internet server container, and only then call it deployed.

.. seealso::

  Both are covered in :doc:`how to migrate the database
  <../how_to/migrate_database>`, which ends with the two commands that have to
  follow the migration.

To enter the container for any service, execute this command.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec <service_name> sh

.. note::

  ``sh`` works in every image. Every one of them except the reverse proxy is
  built off Debian and also has ``bash``, which is the nicer shell of the two;
  the reverse proxy is built off Alpine and has only ``sh``.

From time to time, you will have to enter the Django container to make and run
migrations, collect static files and do the occasional housekeeping.

Relax.
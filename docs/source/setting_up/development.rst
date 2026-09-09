:sourcefiles:
  omniport-docker/scripts/start/development.sh
  omniport-backend/scripts/start/django.sh
  omniport-frontend/scripts/start/react.sh

Development
===========

With everything set up, the flows diverge. This is how to develop for Omniport.

Sysadmin
--------

As ``apps``, enter ``omniport-docker/``. Set up all the shared services.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/start/development.sh

This starts the database, the cache and the message broker. Being heavy and all,
every developer shares these services.

.. warning::

  That script does not start everything Omniport needs. Five separate Redis
  instances back the session store, the channel layer and three caches, and a
  Django server that cannot reach the session store answers every request with
  a 500, signed in or not. Nothing fails while starting, so the omission shows
  up only in the browser. Start them as well.

.. code-block:: console

  [apps omniport-docker]$ docker-compose up -d channel-layer session-store \
      communication-store verification-store application-store

To enter the container for any service, execute this command.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec <service_name> bash

.. note::

  Every Omniport image except the reverse proxy is built off Debian and has
  ``bash``. The reverse proxy is built off Alpine and has only ``sh``.

Go as a developer and migrate the services.

Relax.

Developer
---------

As ``dev1``, clone the following.

- ``omniport-backend``
- ``omniport-frontend``
- all services on the backend and frontend
- your apps on the backend and frontend

Then from ``omniport-backend/``, start your development server.

.. code-block:: console

  [dev1 omniport-backend]$ ./scripts/start/django.sh

Note the port that you are assigned. Let's call it ``<django_port>``.

Then from ``omniport-frontend/``, start your development server.

.. code-block:: console

  [dev1 omniport-frontend]$ ./scripts/start/react.sh -d <django_port>

.. note::

  The React script attaches itself to a Django container named ``60000``, which
  is the first port the Django script hands out. A Django server has to be
  running on that port, though not necessarily yours, before any React server
  will start. If you are the only developer on the machine, start Django first
  and you will have it.

Visit these ports from your browser and you should be able to see your app.
Changing code in either codebase will automatically reload the servers.

To enter the container for any server, execute this command.

.. code-block:: console

  [dev1 anywhere]$ docker exec -ti <port> sh

.. note::

  Both development servers are built off Debian, so ``bash`` works directly and
  there is no need to reach it through ``sh``.

From time to time, you will have to enter the Django container to make and run
migrations, collect static files and do the occasional housekeeping. You should
migrate only your own apps. Apps migrated by ``dev2`` should not be migrated by
``dev1``. In most sane cases, this situation will never even arise.

Have fun!

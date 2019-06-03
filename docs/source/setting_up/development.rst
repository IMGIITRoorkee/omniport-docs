Development
===========

With everything set up, the flows diverge. This is how to develop for Omniport.

Sysadmin
--------

As ``apps``, enter ``omniport-docker/``. Set up all the shared services.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/start/development.sh

This should start all shared services such as the database and message-broker.
Being heavy and all, every developer shares these services.

To enter the container for any service, execute this command.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec <service_name> bash

.. note::

  Most Omniport services are built off of Debian and have ``bash`` installed. In
  case, you face trouble, try running ``sh`` instead.

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

Note the port that you are assigned Let's call it ``<django_port>``.

Then from ``omniport-frontend/``, start your development server.

.. code-block:: console

  [dev1 omniport-frontend]$ ./scripts/start/react.sh -d <django_port>

Visit these ports from your browser and you should be able to see your app.
Changing code in either codebase will automatically reload the servers.

To enter the container for any server, execute this command.

.. code-block:: console

  [dev1 anywhere]$ docker exec -ti <port> sh

.. note::

  Some services, namely those built off of Debian, have ``bash`` installed. Most
  don't. So the best way to go about it is to execute ``sh`` and once in the 
  container, execute ``bash``.

From time to time, you will have to enter the Django container to make and run
migrations, collect static files and do the occasional housekeeping. You should
migrate only your own apps. Apps migrated by ``dev2`` should not be migrated by
``dev1``. In most sane cases, this situation will never even arise.

Have fun!

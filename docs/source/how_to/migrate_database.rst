:sourcefiles:
  omniport-backend/omniport/omniport/settings/base/discovery.py
  omniport-backend/omniport/core/kernel/management/commands/collectdaemon.py

... migrate database?
=====================

Before you can make any use of Omniport, you'll need to migrate the database.
This can be accomplished with the usual ``migrate`` command from inside the
intranet or Internet server container.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec intranet-server bash
  docker@intranet-server:/omniport$ python manage.py migrate <app_name>

In a regular classic Django setup you could very easily skip <app_name> and 
migrate every installed app automatically. Unfortunately, our use of swappable
models makes that a little complicated.

.. warning::

  Because of the same reason as stated above, the use of a shell must be
  thoroughly debated and determined beforehand. After the migration, a shell
  cannot be inserted or removed without a complete reset of the database.

You will need to migrate apps individually and in a strictly defined order. This
is as follows.

#. kernel, which brings ``contenttypes``, ``auth``, ``base_auth`` and, if you
   have installed one, ``shell`` along with it
#. base_auth
#. shell, if you have installed one
#. formula_one
#. auth
#. session_auth
#. token_auth
#. sessions
#. open_auth
#. oauth2_provider
#. admin
#. guardian
#. django_celery_results

.. note::

  ``kernel`` depends on the *first* migration of ``base_auth`` and of ``shell``,
  not on every migration either of them ships. Migrating ``kernel`` therefore
  leaves both only partly applied, which is why they appear in the list in
  their own right. ``formula_one`` and ``token_auth`` are depended upon by
  nothing at all, so they are only ever migrated by being named.

After the above have been migrated, you have a fully functional Omniport core.
But that is not all, you'll also have to migrate the following before the 
installation can be of any use.

#. *any remaining services*
#. *any remaining apps*

At any time during the migration process, run the following command to see what
has been migrated and what is left to be migrated.

.. code-block:: console

  docker@intranet-server:/omniport$ python manage.py showmigrations

Once ``showmigrations`` reports nothing left unapplied, the database is ready.

After migrating
---------------

A migrated database is not yet a working portal. Two further commands have to
be run in the same container, and neither of them runs for you at startup.

.. code-block:: console

  docker@intranet-server:/omniport$ python manage.py collectstatic
  docker@intranet-server:/omniport$ python manage.py collectdaemon

``collectstatic`` gathers the static files of every discovered service and app
into the volume that the reverse proxy serves.
Without it the portal loads, but every stylesheet, script and image below
``/static/`` answers with a 404, which includes the Django admin and the
browsable API.

``collectdaemon`` symlinks the Supervisor configuration that services and apps
ship into the directory Supervisor reads when it starts.
Without it no background worker is ever started, the Celery worker included, so
tasks queue up and never run.

.. note::

  Run both again whenever you add a service or an app, and restart the server
  containers after ``collectdaemon`` so that Supervisor reads the new
  configuration.

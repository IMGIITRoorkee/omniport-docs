... migrate database?
=====================

Before you can make any use of Omniport, you'll need to migrate the database.
This can be accomplished with the usual ``migrate`` command. from inside the
intranet or Internet server container.

.. code-block:: python

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

#. kernel (will automatically migrate contenttypes, auth, base_auth and shell)
#. auth
#. session_auth
#. sessions
#. open_auth
#. oauth2_provider
#. admin
#. guardian

After the above have been migrated, you have a fully functional Omniport core.
But that is not all, you'll also have to migrate the following before the 
installation can be of any use.

#. *any remaining services*
#. *any remaining apps*

At any time during the migration process, run the following command to see what
has been migrated and what is left to be migrated.

.. code-block:: console

  docker@intranet-server:/omniport$ python manage.py showmigrations

That's it. Now you have a fully migrated database and are ready to populate it.
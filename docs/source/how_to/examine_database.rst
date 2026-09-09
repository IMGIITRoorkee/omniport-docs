:sourcefiles:
  omniport-docker/postgres/database_stencil.env
  omniport-docker/docker-compose.yml

... examine database?
=====================

While the Django ORM is beautiful in its capabilities and allows you to interact
with the database in wonderfully Pythonic ways, there are always times when you
have to get your hands dirty and enter the belly of the beast known as Postgres.

That's also simple to do in Omniport. Just enter the following command into the
shell and you'll be dropped into the PostgreSQL prompt where you can issue SQL
queries to your heart's content.

.. code-block:: console

  [apps omniport-docker]$ docker-compose exec database psql -U <user> -d <db>
  
Here <db> and <user> must be replaced with the values of POSTGRES_DB and
POSTGRES_USER respectively, as written in the file ``postgres/database.env``.

Here on out, refer to the PostgreSQL documentation for help.

.. warning::

  Omniport swaps several of its core models, so the table a model writes to is
  not always the one its name suggests. If you have installed a shell, the rows
  behind ``Person``, ``Student`` and their neighbours live in the shell's
  tables and the ``kernel`` ones sit unused. Read
  :doc:`the migration guide <migrate_database>` before you write anything, and
  prefer ``SELECT`` until you are certain which table is live.

.. warning::

  Omniport ships no backup mechanism. The Compose file declares volumes named
  ``database_backup``, ``media_files_backup`` and ``personal_files_backup``,
  but no container mounts them and nothing ever writes to them, so the names
  promise a safety net that does not exist. Arrange your own ``pg_dump``
  schedule before you run anything of consequence against a live database.

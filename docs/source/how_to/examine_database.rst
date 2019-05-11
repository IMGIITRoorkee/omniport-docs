... examine database?
=====================

While the Django ORM is beautiful in its capabilities and allows you to interact
with the database in wonderfully Pythonic ways, there are always times when you
have to get your hands dirty and enter the belly of the beast known as Postgres.

That's also simple to do in Omniport. Just enter the following command into the
shell and you'll be dropped into the PostgreSQL prompt where you can issue SQL
queries to your heart's content.

.. code-block:: console

  [apps omniport-docker]$ dc exec database psql -U <user> -d <db>
  
Here <db> and <user> must be replaced with the values of POSTGRES_DB and
POSTGRES_USER respectively, as written in the file ``postgres/database.env``.

Here on out, refer to the PostgreSQL documentation for help.
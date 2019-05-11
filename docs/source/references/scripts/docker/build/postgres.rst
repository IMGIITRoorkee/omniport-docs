PostgreSQL
==========

This script builds the PostgreSQL container that acts as the primary database for
all Omniport apps and services.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/postgres.sh

You will get the choice regarding the recreation of the database environment
file. Affirm with a :kbd:`Y` if you intend to rewrite it, else decline with any
other character, primarily :kbd:`N`.

.. warning::

  If this is your first time building the container, choose :kbd:`Y`. Choosing
  :kbd:`N` can have adverse unwanted consequences.

If you choose to recreate the environment file, you will have to answer a
questionnaire. Enter a database name, a username and a password for the
database.

Remember to populate this database name, username and password in the
:doc:`Django project-level configuration file
<../../../config_files/project/base_yml>`.
RabbitMQ
========

This script builds the RabbitMQ container that acts as the message-broker for
all Omniport apps and services.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/rabbitmq.sh

You will get the choice regarding the recreation of the message broker
environment file. Affirm with a :kbd:`Y` if you intend to rewrite it, else
decline with any other character, primarily :kbd:`N`.

.. warning::

  If this is your first time building the container, choose :kbd:`Y`. Choosing
  :kbd:`N` can have adverse unwanted consequences.

If you choose to recreate the environment file, you will have to answer a
questionnaire. Enter a username and a password for the message broker.

Remember to populate this username and password in the :doc:`Django project-level
configuration file <../../../config_files/project/base_yml>`.
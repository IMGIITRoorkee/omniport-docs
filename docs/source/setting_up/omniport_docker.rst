Omniport Docker
===============

Clone Omniport Docker from 
`GitHub <https://github.com/IMGIITRoorkee/omniport-docker.git/>`_
and enter the directory.

Inside the directory ``omniport-docker/`` you must clone the codebase of 
Omniport, namely the backend and the frontend. Create a ``codebase/`` directory,
enter it, and then clone both ``omniport-backend`` and ``omniport-frontend``
repositories from GitHub. 

.. warning::

  Keep the clone of ``omniport-docker`` under that name. The scripts that start
  the development servers attach to a Docker network whose name Compose derives
  from the directory the project sits in, and they spell that name out in full.
  Rename the directory and every developer's server fails to start.

.. note::

  You may use the 
  :doc:`clone codebase script <../references/scripts/docker/clone/everything>` 
  to accomplish the same goal. It deletes and recreates ``codebase/`` before it
  starts, so run it before you write any configuration rather than after, and
  never on an instance you have already set up.

Configuring the environment
---------------------------

RabbitMQ
++++++++

In ``rabbitmq/``, copy ``message_broker_stencil.env`` to ``message_broker.env``
and populate the environment variables. These will be used when the queue is set
up so choose a strong password.

You will need to provide these values in the Django configuration, so remember
them.

PostgreSQL
++++++++++

In ``postgres/``, copy ``database_stencil.env`` to ``database.env`` and populate
the environment variables. These will be used when the database management
system is set up so choose a strong password.

You will need to provide these values in the Django configuration, so remember 
them.

Django
++++++

Django configuration works at two levels:

- base-level configuration
- site-level configuration

Enter ``codebase/omniport-backend/configuration/``.

Base-level configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Copy ``base_stencil.yml`` to ``base.yml`` and populate all the variables there.
If you need help, refer to the :doc:`documentation on this file
<../references/config_files/project/base_yml>`.

Site-level configuration
~~~~~~~~~~~~~~~~~~~~~~~~

In ``sites/``, copy ``site_stencil.yml`` to

- ``site_0.yml`` in development
- ``site_1.yml`` and ``site_2.yml`` in production

and populate all the variables there. If you need help, refer to the
:doc:`documentation on this file <../references/config_files/project/site_yml>`.

NGINX
+++++

There is no configuration file to write here. Just keep the domain names for
the Intranet site and the Internet site at hand. If you have SSL enabled, which
you absolutely should because it enhances security and is absolutely free, place
your 

- certificate named ``omniport.crt``
- private key named ``omniport.key``

in the directory ``cert/``.

Also, if you choose the SSL route, remember to answer 'yes' for HTTPS in the 
NGINX image build script.

Build the Dockerfiles
---------------------

There are quite a few images to be built which, thanks to Omniport's liberal use
of scripts, translates to executing just as many shell commands. Most of these
scripts are interactive, which means you will be asked questions, whose answers
will determine the end result of the operation. Build them after cloning the
codebase, not before, because two of them copy dependency manifests out of it.

Maybe one day we will write a script that runs these scripts.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/django.sh
  [apps omniport-docker]$ ./scripts/build/react.sh
  [apps omniport-docker]$ ./scripts/build/nginx.sh
  [apps omniport-docker]$ ./scripts/build/memcached.sh
  [apps omniport-docker]$ ./scripts/build/rabbitmq.sh
  [apps omniport-docker]$ ./scripts/build/postgres.sh
  [apps omniport-docker]$ ./scripts/build/redis.sh
  
That's all. Omniport Docker is ready to roll.

.. note::

  The React image is not one of the containers Omniport runs. It exists so that
  the frontend can be built inside it, which is the first step of
  :doc:`deploying <production>`, so build it here even though nothing in the
  Compose file uses it.

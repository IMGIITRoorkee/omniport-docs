Server configuration
====================

To start up, use a fresh installation of your favourite operating system. This 
could be any flavour of Linux, such as Ubuntu, Fedora or RHEL, to name a few.

Ports
-----

Ensure that no other services are running on the ports specified below, 
especially those marked with an asterisk.

=============== =====================
 Port            Designated use
=============== =====================
 80*             NGINX http
 443*            NGINX https
 5432            PostgreSQL
 5672            RabbitMQ
 15672*          RabbitMQ management
 11211           Memcached
 6379            Redis
 8000            Gunicorn
 8001            Daphne
 8081*           Redis Commander
 60000 - 60031   Django development
 61000 - 61031   React development
=============== =====================

In the most common scenarios, 80 and 443 will be occupied on a fresh install 
of a server distribution like RHEL or Ubuntu Server. Stop Apache2 and prevent
it from automatically starting up again.

.. code-block:: console

  [apps ~]$ sudo systemctl stop apache2
  [apps ~]$ sudo systemctl disable apache2

Users
-----

Set up a user other than ``root`` to build and manage the containers. Name him 
``apps`` or whatever you fancy.

In case of a development setup, make user accounts for all your developers, one
per person. Let's assume you have two ``dev1`` and ``dev2``. They also get
their own directories at ``/home/dev1/`` and ``/home/dev2/``.

.. code-block:: console

  [dev1 ~]$ whoami
  dev1
  [dev1 ~]$ pwd
  /home/dev1

.. code-block:: console

  [dev2 ~]$ whoami
  dev2
  [dev2 ~]$ pwd
  /home/dev2


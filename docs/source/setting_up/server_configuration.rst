Server configuration
====================

To start up, use a fresh installation of your favourite operating system. This 
could be any flavour of Linux, such as Ubuntu, Fedora or RHEL, to name a few.

Ports
-----

Only some of the ports Omniport uses are bound on the host. Those are the ones
that have to be free before you start. The rest are reached over the container
network, and something else on the host may hold them without any conflict
arising.

Bound on the host
+++++++++++++++++

=============== =======================================
 Port            Designated use
=============== =======================================
 80              NGINX http
 443             NGINX https
 15672           RabbitMQ management
 60000 - 60031   Django development, one per developer
 61000 - 61031   React development, one per developer
=============== =======================================

The two ranges at the end are bound only on a development machine, and only one
port from each is taken per running server.

Internal to the container network
+++++++++++++++++++++++++++++++++

=============== ====================================
 Port            Designated use
=============== ====================================
 5432            PostgreSQL
 5672            RabbitMQ
 11211           Memcached
 6379            Redis, on each of its five instances
 8000            Gunicorn
 8001            Daphne
=============== ====================================

If a web server is already running on the machine it will be holding 80 and
443, and it has to be stopped and kept from starting again. The unit is named
``apache2`` on Debian and Ubuntu and ``httpd`` on RHEL and Fedora.

.. code-block:: console

  [apps ~]$ sudo systemctl stop apache2
  [apps ~]$ sudo systemctl disable apache2

Users
-----

Set up a user other than ``root`` to build and manage the containers. Name it 
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


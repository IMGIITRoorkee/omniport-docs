Docker
======

Once you have configured the server, it's time to install the Docker CE suite on
it. Setting up Docker is easy. Since that is beyond the scope of the
documentation, please refer to the Docker documentation for instructions
pertaining to your operating system.

Do note that installing Docker alone will not suffice, you will also need to 
install Docker Compose.

.. note::

  The Docker 
  `documentation <https://docs.docker.com/>`_
  contains the links to install Docker and Docker Compose on your system of 
  choice.

.. warning::

  Omniport's scripts call ``docker-compose``, with a hyphen, which is the first
  version of Compose. Current Docker packages ship the second version instead,
  invoked as ``docker compose`` with a space, and do not provide the hyphenated
  command at all. On such an installation every Compose command in this
  documentation fails with ``docker-compose: command not found`` until you
  either install the standalone binary or put a shim of that name on the path.

Start and enable Docker
-----------------------

After you have installed Docker and Docker Compose on your machine, you will 
need to make some configuration changes.

Docker has been installed but the daemon is neither running nor has been set to
run automatically on a reboot. You can accomplish these changes as follows.

.. code-block:: console

  [apps ~]$ sudo systemctl start docker
  [apps ~]$ sudo systemctl enable docker

Groups
------

The Docker daemon process ``dockerd`` is only accessible to users that are a 
part of the Docker group. 

Remember ``apps`` from :doc:`Environments <../environments/index>` and
:doc:`server configuration <server_configuration>`? So ``apps`` must be a member
of the group ``docker``, which is automatically created when Docker is first
installed.

.. warning::

  Membership of the ``docker`` group is equivalent to being root on the host.
  Anyone in it can start a container that mounts the whole filesystem and runs
  as root inside it, which is unrestricted access by another name. Grant it as
  deliberately as you would grant ``sudo``, and read the development section
  below with that in mind, because it puts every developer in the same group.

.. code-block:: console

  [apps ~]$ sudo usermod -aG docker apps

Also in a development environment, your developers must also be members of the
group.

.. code-block:: console

  [apps ~]$ sudo usermod -aG docker dev1
  [apps ~]$ sudo usermod -aG docker dev2

You will need to restart your user sessions, and in my personal experience in 
some cases, even restart your computer, after this.

User namespaces
---------------

User namespaces are a way to limit the surface area of the Docker sandbox in 
the event of a security breach. Basically user namespaces map ``root`` in the 
Docker sandbox to another UID on the host, thereby stripping away all rights of
the root user in a container to cause damage to the host.

.. warning::

  While user namespaces are very cool and good, we at IMG have run into a number 
  of intermittent and irregularly occurring issues when running Omniport under a 
  namespace. This step is therefore advised only for people who know what they
  are doing.

To enable namespaces, elevate your privileges, open the file 
``/etc/docker/daemon.json`` and type in the following lines.

.. code-block:: json

  {
    "userns-remap": "apps"
  }

If you decided to go with an alternative name for the main user, replace 
``apps`` with the username of that user.

.. note::

  Remapping applies to the daemon as a whole, but the scripts that start the
  development servers opt themselves out of it, because a remapped root would
  give the wrong ownership to the source tree they mount from the host. So the
  containers a developer runs are not remapped even when the setting is on, and
  only the ones Compose starts are.

You will need to restart the Docker daemon after this change.

.. code-block:: console

  $ sudo systemctl restart docker

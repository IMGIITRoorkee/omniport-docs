Folder structure
================

Omniport follows this outline of folder configuration. Omniport Docker houses
both sides of the codebase in a ``codebase/`` folder.

::

  omniport-docker
  ├── docker-compose.yml
  ├── cert
  │   └── ...
  ├── scripts
  │   └── ...
  ├── tests
  │   └── ...
  ├── django
  │   ├── Dockerfile
  │   └── ...
  ├── react
  │   ├── Dockerfile
  │   └── ...
  ├── nginx
  │   ├── Dockerfile
  │   └── ...
  ├── postgres
  │   ├── Dockerfile
  │   └── ...
  ├── redis
  │   ├── Dockerfile
  │   └── ...
  ├── memcached
  │   ├── Dockerfile
  │   └── ...
  ├── rabbitmq
  │   ├── Dockerfile
  │   └── ...
  └── codebase
      ├── omniport-backend
      │   ├── scripts
      │   │   └── ...
      │   ├── omniport
      │   │   ├── core
      │   │   ├── shell*
      │   │   ├── services
      │   │   ├── apps
      │   │   └── ...
      │   └── ...
      └── omniport-frontend
          ├── scripts
          │   └── ...
          ├── omniport
          │   ├── core
          │   ├── formula_one
          │   ├── services
          │   ├── apps
          │   └── ...
          └── ...

Every directory that holds a ``Dockerfile`` is an image that one of the build scripts builds, and ``cert/`` is where the reverse proxy looks for its TLS certificate and key.

.. note::

  These trees show a codebase that has been cloned in full, not the one you get from a single ``git clone``.
  The ``shell``, ``formula_one``, ``services/`` and ``apps/`` directories are filled in by the clone scripts, so a fresh checkout is missing them until you run those.

  The asterisk on ``shell`` marks it as optional.
  It is cloned only if you ask for it, and Omniport runs unshelled without it.

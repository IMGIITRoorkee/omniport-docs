Folder structure
================

Omniport follows this outline of folder configuration. Omniport Docker houses
both sides of the codebase in a ``codebase/`` folder.

::

  omniport-docker
  ├── docker-compose.yml
  ├── scripts
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
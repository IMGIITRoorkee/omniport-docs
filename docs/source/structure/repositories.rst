Repositories
============

Omniport is not a single repository. The entire project is made up
of dozens of distinct, yet interconnected parts, most of which have their own
repositories under the `IMGIITRoorkee <https://github.com/IMGIITRoorkeee>`_   
GitHub organisation page. This means that cloning the Omniport project is not 
one operation but many.

The essential ones of these repositories are explained here.

Infrastructure
--------------

This repository contains the code that drives the Omniport infrastructure.
That means that all ``Dockerfiles``, environment variables and build scripts
are kept in this repository.

.. image:: https://img.shields.io/badge/omniport-infrastructure-red.svg?style=flat-square
  :target: https://github.com/IMGIITRoorkee/omniport-docker/

.. image:: https://img.shields.io/github/license/IMGIITRoorkee/omniport-docker.svg?style=flat-square&logo=github&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-docker/

.. image:: https://img.shields.io/github/last-commit/IMGIITRoorkee/omniport-docker.svg?style=flat-square&logo=docker&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-docker/

Codebase
--------

Omniport backend
++++++++++++++++

This repository contains the code of the Omniport backend architecture,
written in Django on Python. This includes all the core functionality of
the project and is extensible in terms of choosing your own set of apps to 
run on it.

This backend can be customised and branded according to your own wishes.
All configuration and branding lies in directories outside the code so that 
you do not have to know development to set the project up.

.. image:: https://img.shields.io/badge/omniport-backend-orange.svg?style=flat-square
  :target: https://github.com/IMGIITRoorkee/omniport-backend/

.. image:: https://img.shields.io/github/license/IMGIITRoorkee/omniport-backend.svg?style=flat-square&logo=github&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-backend/

.. image:: https://img.shields.io/github/last-commit/IMGIITRoorkee/omniport-backend.svg?style=flat-square&logo=django&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-backend/

Omniport frontend
+++++++++++++++++

This repository contains the code of the Omniport frontend architecture,
written in React on JavaScript. This includes all the core functionality of
the project and can be extended with apps, that are independent of the 
backend.

This frontend takes all the customisations from the backend and is therefore
totally branding-ready and tweakable. All changes on the backend are 
reflected here with very little to almost no effort.

.. image:: https://img.shields.io/badge/omniport-frontend-yellow.svg?style=flat-square
  :target: https://github.com/IMGIITRoorkee/omniport-frontend/

.. image:: https://img.shields.io/github/license/IMGIITRoorkee/omniport-frontend.svg?style=flat-square&logo=github&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-frontend/

.. image:: https://img.shields.io/github/last-commit/IMGIITRoorkee/omniport-frontend.svg?style=flat-square&logo=react&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-frontend/

Shell
-----

As we previously mentioned, Omniport is a portal that is epically generic. 
Any institute around the world, from Fiji to Fiji the other way, can set it
up and get going.

But if your institute has the technical know-how that a group like IMG 
provides IIT Roorkee, you can easily *swap* out models in the ``kernel``
module of ``omniport-backend`` with your own. You can also *switch* out the
serializers in the ``kernel`` module with your own.

This swap and switch functionality can be made use of to develop shells for
the backend as we have made one for our institute. You are free to refer to 
it to make your own, or run the fully functional, unshelled versions of the 
software.

.. image:: https://img.shields.io/badge/omniport-shell-blue.svg?style=flat-square
  :target: https://github.com/IMGIITRoorkee/omniport-shell/

.. image:: https://img.shields.io/github/license/IMGIITRoorkee/omniport-shell.svg?style=flat-square&logo=github&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-shell/

.. image:: https://img.shields.io/github/last-commit/IMGIITRoorkee/omniport-shell.svg?style=flat-square&logo=django&logoColor=white
  :target: https://github.com/IMGIITRoorkee/omniport-shell/

.. note::

  Other than the shell for **Indian Institute of Technology, Roorkee**, any 
  shells made for Omniport are not under the purview of Information Management 
  Group.  
  
  IMG couldn't possibly take responsibility for the upkeep, maintenance or 
  upgradation of any random shells made by any random developers for any random
  institutes of any random country.

Sub-components
--------------

Apart from these repositories are Omniport itself, there are a huge number of 
repostories that are a part of Omniport. These are apps and services.

Every single one of Omniport's many apps and services resides in its own 
repository. They follow a naming convention as follows.

- ``omniport-service-<service>`` and ``omniport-frontend-<service>``
- ``omniport-app-<app>`` and ``omniport-frontend-<app>``

Totalled, these repositories number in the fifties. But since these are on an
open architecture, there is total democracy and freedom regarding who can create
apps and what those apps can provide. This number has no upper limit.
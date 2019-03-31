Architecture
============

We, the developers of Omniport, pride ourselves on Omniport's architecture. It
is a smart blend of automation and explicitness. We strive to make Omniport as
automated as possible to reduce the amount of code a person has to write to set
it up and extend it, but at the same time not be too *magical* for an ordinary
person to understand, in detail, its functionality.

Omniport, at its very core, contains a distinction between apps and services.
Apps and services are all Django applications, there is but an ideological
difference between the two categories.

Services
--------

Services are Django apps that provide critical functionality. Services may 
depend on other services and on the core. A service may not depend on an app.
Services may depend on other services, which is strongly encouraged because it
leads to a cohesive system.

All services must be installed for Omniport to function properly. Services 
cannot be chosen at will. Services do not contain any form of filtering based
on user roles, corresponding active statuses, or IP addresses.

Services, and services only, may appear in the Omniport sidebar. The subset of
services that appear in the sidebar are defined by their ``config.json`` file on
the frontend.

.. seealso:: 
  
  More on frontend configuration files
  :doc:`here <../references/config_files/app/config_json>`.

For an example, consider the service 'Developer', which is used by developers to
develop OAuth2 based applications on Omniport.

Services are cloned into ``services/`` directories inside the src directory
(``omniport/``) in both the backend and frontend codebases.

Since there is no mix-and-match capability in Omniport services, the process 
of cloning services has been merged with the cloning of the codebases
using the ``clone_codebase.sh`` script provided by ``omniport-docker``.

.. seealso::

  More on the ``clone-codebase.sh`` script
  :doc:`here <../references/scripts/docker/clone/everything>`.

Apps
----

Apps are extensions to Omniport that provide new functionality. Apps may depend
on other apps, which is strongly discouraged because it may lead to crashes when
dependencies are forgotten, or on services, which is strongly encouraged because
it leads to a cohesive system.

Apps can be plugged into the Omniport system as and if needed or wanted. Apps
can be chosen at will.

All apps can choose their target demographic on the basis of roles and 
corresponding active statuses. These filters can be configured in the 
``config.yml`` file on the backend. This leads to every user seeing a set of 
apps on the backend.

.. seealso:: 
  
  More on backend configuration files
  :doc:`here <../references/config_files/app/config_yml>`.

.. math::

  A = \{\text{apps allowed to a user based on role, active status and orgin IP address}\}

Then there is a set of apps whose frontend has been installed in the frontend
architecture. This leads to a second set of apps common to every user. 

.. math::
  
  B = \{\text{all apps installed on the frontend}\}

The net set of apps that any user sees is the intersection of both these sets.

.. math::

  Result = A \cap B

Apps are cloned into ``apps/`` directories inside the src directory 
(``omniport/``) in both the backend and frontend codebases.

Dependencies
------------

::

  service ---may depend on--> core
  service ---may depend on--> service
  app     ---may depend on--> core
  app     ---may depend on--> service

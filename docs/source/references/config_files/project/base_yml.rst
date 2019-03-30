``base.yml`` on the backend
===========================

Purposes
--------

``base.yml`` is the top-level of customisation that can be achieved with 
Omniport. The values specified here determine a lot of things about how Omniport
behaves and responds.

Branding
++++++++

The branding part of the config file is used to define the branding of the 
Omniport project, mainly the textual aspect of branding. It requires the 
``branding`` key to be defined in ``base.yml``.

:branding:
  | Branding related fields of the project
  | ``{object}`` which has the following subkeys

  :institute:
    | Attributes pertaining to the brand of the institute hosting the portal
    | ``{object}`` which has the following subkeys

      :acronym:
      | Acronyms of institutes which have long names
      | ``string``

      :name:
      | The full name of the institute
      | ``string``

      :homePage:
      | The URL to the home page of the institute on the web
      | ``string``

  :maintainers:
    | Attributes pertaining to the brand of the maintainers behind the portal
    | ``{object}`` which has the following subkeys

      :acronym:
      | Acronyms of maintainer groups which have long names
      | ``string``

      :name:
      | The full name of the maintainer group
      | ``string``

      :homePage:
      | The URL to the home page of the maintainer group on the web
      | ``string``

Internationalisation
++++++++++++++++++++

The internationalisation part of the config file is simply to customise the 
language and timezone of the project.

:i18n:
  | Internationalisation related fields of the project
  | ``{object}`` which has the following subkeys

  :languageCode:
    | The languge code of the portal
    | ``string``

  :timeZone:
    | The languge code of the portal
    | ``string``

Secrets
+++++++

Secrets pertaining to the Omniport project, such as passwords, client IDs and 
most importantly the Django secret key go here.

:secrets:
  | Secrets of the Omniport project
  | ``{object}`` which has the following subkeys

  :secretKey:
    | The Django secret key of the project
    | ``string``

Services
++++++++

As Omniport depends on a lot of services for optimum functioning, we made a
Docker project to make the setup easy. If you use the Docker project, a lot of
these settings have to be their default values as shown in the
``base_stencil.yml`` file. If you have tweaked them, fill these sections out.

:services:
  | Credentials to connect to all Omniport dependencies
  | ``{object}`` which has the following subkeys

  :database:
    | Attributes pertaining to database service
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``

      :user:
      | The username that can be used to log in to the service
      | ``string``

      :password:
      | The password for the given user
      | ``string``

      :name:
      | The name of the database to use
      | ``string``

  :messageBroker:
    | Attributes pertaining to message broker service
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``

      :user:
      | The username that can be used to log in to the service
      | ``string``

      :password:
      | The password for the given user
      | ``string``

  :channelLayer:
    | Attributes pertaining to Redis container supporting Django Channels
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``

  :sessionStore:
    | Attributes pertaining to Redis container storing sessions
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``

  :notificationStore:
    | Attributes pertaining to Redis container storing notifications
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``

  :cache:
    | Attributes pertaining to the Memcached cache
    | ``{object}`` which has the following subkeys

      :host:
      | The IP/name of the host machine or container running this service
      | ``string``

      :port:
      | The port on which the service can be reached
      | ``string``
    
IP address rings
++++++++++++++++

Omniport being the web portal serves a number of clients on different levels of
the network. There is the server itself, a close cluster of servers working
together, certain cabinet computers that can connect to the server, the lab of
the maintainer group, the intranet and then the Internet at large.

These clients can be arranged into rings, where the innermost rings have the 
highest priority in terms of privilege to access certain APIs and resources.

These rings are described here, in the ``ipAddressRings`` key.

:ipAddressRings:
  | Hello
  | ``[{object}]`` each of which has the following subkeys 

  :name:
    | The name of this IP address ring, the identifier for this ring
    | ``string``

  :patterns:
    | The regex of the IP pattern that falls in the level
    | ``[string]``

Examples
--------
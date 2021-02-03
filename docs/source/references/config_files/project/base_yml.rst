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
        | ``integer``

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
        | ``integer``

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
        | ``integer``

  :sessionStore:
    | Attributes pertaining to Redis container storing sessions
    | ``{object}`` which has the following subkeys

      :host:
        | The IP/name of the host machine or container running this service
        | ``string``

      :port:
        | The port on which the service can be reached
        | ``integer``

  :communicationStore:
    | Attributes pertaining to Redis container storing communications
    | ``{object}`` which has the following subkeys

      :host:
        | The IP/name of the host machine or container running this service
        | ``string``

      :port:
        | The port on which the service can be reached
        | ``integer``

  :verificationStore:
    | Attributes pertaining to Redis container storing verifications
    | ``{object}`` which has the following subkeys

      :host:
        | The IP/name of the host machine or container running this service
        | ``string``

      :port:
        | The port on which the service can be reached
        | ``integer``

  :notificationStore:
    | Attributes pertaining to Redis container storing notifications
    | ``{object}`` which has the following subkeys

      :host:
        | The IP/name of the host machine or container running this service
        | ``string``

      :port:
        | The port on which the service can be reached
        | ``integer``

  :applicationStore:
    | Attributes pertaining to Redis container storing data for omniport
    | applications which are temporary in nature
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
        | ``integer``
    
Integrations
++++++++++++++++

Useful applications that can connect to Django, like `Sentry
<https://sentry.io/welcome/>`_, can be integrated into the project.

Emails
++++++++++++++++

The emails part of the config file is used to define settings for sending
emails from your project.

:emails:
  | Email configurations for your project
  | ``{object}`` which has the following subkeys

    :emailBackend:
      | The backend used for sending emails
      | ``string``

    :emailHost:
      | The email service provider used
      | ``string``

    :emailUseTls:
      | Whether an email uses a TLS connection or not
      | ``boolean``

    :emailPort:
      | The port used by smtp server
      | ``integer``

    :emailHostUser:
      | The email address from which all emails will be sent
      | ``string``

    :emailHostPassword:
      | The password of the host's email account
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
  | ``[{object}]`` each of which has the following subkeys 

  :name:
    | The name of this IP address ring, the identifier for this ring
    | ``string``

  :patterns:
    | The regex of the IP pattern that falls in the level
    | ``[string]``

Examples
--------

A fully equipped ``base.yml`` file, with all settings populated looks quite like
this.

.. code-block:: yaml

  branding:
    institute:
      acronym: IIT-R
      name: Indian Institute of Technology Roorkee
      homePage: https://iitr.ac.in/
    maintainers:
      acronym: IMG
      name: Information Management Group
      homePage: https://channeli.in/img/
  i18n:
    languageCode: en-gb
    timeZone: Asia/Kolkata
  secrets:
    secretKey: '2)@2klj=@a(*o9kyt7u^!g4jbqrqo3$ju^o_g6n*lh-d$$#zdy'
  services:
    database:
      host: database
      port: 5432
      user: omniport_user
      password: omniport_password
      name: omniport_database
    channelLayer:
      host: channel-layer
      port: 6379
    sessionStore:
      host: session-store
      port: 6379
    communicationStore:
      host: communication-store
      port: 6379
    verificationStore:
      host: verification-store
      port: 6379
    notificationStore:
      host: notification-store
      port: 6379
    applicationStore:
      host: application-store
      port: 6379
    cache:
      host: cache
      port: 11211
    messageBroker:
      host: message-broker
      port: 5672
      user: omniport_user
      password: omniport_password
  emails:
    emailBackend: 'django.core.mail.backends.smtp.EmailBackend'
    emailHost: 'smtp.example.com'
    emailUseTls: True
    emailPort: 587
    emailHostUser: 'no-reply@omniport.com'
    emailHostPassword: 'img@password'
  ipAddressRings:
  - name: self
    patterns:
    - '^172\.18\.0\.1$'
  - name: specifics
    patterns:
    - '^172\.25\.55\.101$'
    - '^172\.25\.55\.219$'
  - name: maintainers
    patterns:
    - '^172\.25\.55\.\d{1}$'
  - name: intranet
    patterns:
    - '.*'
  - name: internet
    patterns:
    - '.*'

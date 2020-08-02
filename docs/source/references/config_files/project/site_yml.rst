``site_<id>.yml`` on the backend
================================

Purposes
--------

``site_<id>.yml`` is cascaded onto base-level customisation on a per-site basis.
The values specified here determine a lot of things about how each sub-site of
Omniport behaves and responds.

You can override the values defined in :doc:`the base config file <base_yml>`. 
In addition, there are certain configuration knobs that make sense to be defined
on a site-level, which are explained below.

Site
++++

Every site in Omniport can be individually customised. 

.. note::

  So far Omniport has support only for two sites. Work is ongoing to expand this
  to as many sites as needed.

Omniport allows you to customise the name, description as well as the debugging
status of every site in the project. This is accomplished by the ``site`` key in
the config file.

:site:
  | The set of fields for branding a site
  | ``{object}`` which has the following subkeys

  :id:
    | The unique ID of the site
    | ``number`` where 0, 1, 2 denote development, intranet and Internet sites

  :nomenclature:
    | The nomenclature pertaining to the site
    | ``{object}`` which has the following subkeys

    :name:
      | The code name of the site
      | ``string``

    :verboseName:
      | The displayed name of the site
      | ``string``

  :debug:
    | Whether to display debug info, should be ``false`` on production sites
    | ``boolean``

  :description:
    | The description of the site, as an aid to help developers find their way
    | ``string``

Allowances
----------

Allowances determine what parts of Omniport each site is allowed to access.
Fields such as the names of apps that are allowed on the site and the hostnames
that the site should respond to go here. This section also determines the
network rings each site is allowed on.

:allowances:
  | The set of allowed entities for any given site
  | ``{object}`` which has the following subkeys

  :hosts:
    | List of domain names that this site is responsible for serving
    | ``[string]``
  
  :apps:
    | List of app names that this site exposes to the users
    | ``[string]``

  :ipAddressRings:
    | List of network rings that are served by the site
    | These names are ring names from :doc:`the base config file <base_yml>`
    | ``[string]``

Examples
--------

A site-level configuration for a typical development site ``site_0.yml`` looks
like this.

.. code-block:: yaml

  site:
    id: 0
    nomenclature:
      name: development
      verboseName: Omniport Dev
    debug: true
    description: Development site for Omniport
  allowances:
    apps: __all__
    ipAddressRings:
    - self
    - specifics
    - administrators
    - maintainers
    - intranet
    - internet

A site-level configuration for a typical production site, more specifically the
Intranet site ``site_1.yml`` looks like this.

.. code-block:: yaml

  site:
    id: 1
    nomenclature:
      name: intranet
      verboseName: Omniport Intranet
    debug: true
    description: Intranet site for Omniport
  allowances:
    hosts:
    - omniport.intranet
    - intranet.channeli.in
    ipAddressRings:
    - intranet
    - maintainers
    - specifics

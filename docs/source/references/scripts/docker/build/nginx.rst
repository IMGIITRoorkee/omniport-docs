NGINX
=====

This script builds the NGINX container that is responsible for operating the 
reverse proxy to the API, that also serves all our static and media files.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/nginx.sh

You will get the choice regarding the recreation of NGINX configuration files.
Affirm with a :kbd:`Y` if you intend to rewrite them, else decline with any
other character, primarily :kbd:`N`. 

.. warning::

  If this is your first time building the container, choose :kbd:`Y`. Choosing
  :kbd:`N` can have adverse unwanted consequences.

If you choose to recreate the configuration files, you will have to answer a
questionnaire. Enter the domain names that you want to refer to the intranet and Internet
sites of the project.

For example, at IIT Roorkee, the hostnames for Omniport are ``channeli.in`` and
``channeli.iitr.ac.in`` from inside and outside the campus respectively.

Also choose whether to enable SSL with a :kbd:`Y` if you have SSL certificates
or with a :kbd:`N` if you don't. The configuration files will be regenerated and
the image built.

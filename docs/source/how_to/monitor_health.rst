:sourcefiles:
  omniport-docker/docker-compose.yml

... monitor health?
===================

Most Omniport containers have healthchecks built into them, which give you a
way to see at a glance whether the pieces behind the portal are answering.
These healthchecks run at 16 minute intervals and are declared to fail only
after four consecutive misses.

The database, the cache, the message broker and all five Redis stores are
checked. The reverse proxy and the two application servers are not, so their
health column stays empty. An empty column means nothing is being measured,
not that the container is well.

The results of the healthchecks can be seen using the ``ps`` command afforded by
Docker Compose.

.. code-block:: console

  [apps omniport-docker]$ docker-compose ps

And there you have it. Container health is mentioned in brackets in the 'State'
column. The state can be one of several values.

:Up (health\: starting):
  the container is inside its two minute grace period and has not been judged
  yet
:Up (healthy):
  the last check succeeded
:Up (unhealthy):
  four checks in a row have failed
:Up:
  with no bracket, meaning this container declares no healthcheck

.. warning::

  A healthcheck every 16 minutes, failing only after four misses, means a
  container that dies can keep reporting ``healthy`` for the better part of an
  hour. Treat this as a periodic sweep rather than as monitoring, and do not
  rely on it to tell you that the portal is down.
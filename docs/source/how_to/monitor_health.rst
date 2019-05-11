... monitor health?
===================

All Omniport containers (except NGINX, so far) have healthchecks built into them
to provide an easy way to monitor the health of containers in real time. These
healthchecks run at 16 minute intervals.

The results of the healthchecks can be seen using the ``ps`` command afforded by
Docker Compose.

.. code-block:: console

  [apps omniport-docker]$ docker-compose ps

And there you have it. Container health is mentioned in brackets in the 'State'
column. The state can be one of several values.

:Up (health\: starting):
  if the health check was run on an upcoming container 
:Up (healthy):
  if the health check was run and reported a success

That's all you need to know to stay updated on the health of your containers!
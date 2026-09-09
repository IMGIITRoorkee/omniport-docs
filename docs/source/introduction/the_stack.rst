:sourcefiles:
  omniport-docker/docker-compose.yml
  omniport-backend/pyproject.toml
  omniport-frontend/omniport/package.json

The stack
=========

Omniport pins its versions rather than chasing the latest of everything.
The backend locks its Python dependencies in ``poetry.lock`` and the frontend locks its JavaScript ones in ``yarn.lock``, so two people who clone the project a month apart get the same stack.
There is no LTS release to track, but there is no rolling upgrade either: a version moves when somebody deliberately moves it.

+-----------------------+-----------------------+---------------------------+
| Sphere                | Sub-sphere            |  Technology               |
+=======================+=======================+===========================+
| **Orchestration**     | *Containers*          |  Docker                   |
+-----------------------+-----------------------+---------------------------+
| **NoSQL databases**   | *Sessions*            |  Redis                    |
+                       +-----------------------+---------------------------+
|                       | *Communications*      |  Redis                    |
+                       +-----------------------+---------------------------+
|                       | *Channels*            |  Redis                    |
+                       +-----------------------+---------------------------+
|                       | *Verification*        |  Redis                    |
+                       +-----------------------+---------------------------+
|                       | *Temporary app*       |  Redis                    |
+                       +-----------------------+---------------------------+
|                       | *Libraries*           |  django-redis             |
|                       |                       |  channels-redis           |
+-----------------------+-----------------------+---------------------------+
| **SQL database**      | *Application*         |  PostgreSQL               |
+                       +-----------------------+---------------------------+
|                       | *Library*             |  psycopg2-binary          |
+-----------------------+-----------------------+---------------------------+
| **Cache**             | *Application*         |  Memcached                |
+                       +-----------------------+---------------------------+
|                       | *Library*             |  pymemcache               |
+-----------------------+-----------------------+---------------------------+
| **Message broker**    | *Application*         |  RabbitMQ                 |
+                       +-----------------------+---------------------------+
|                       | *Library*             |  Celery                   |
+-----------------------+-----------------------+---------------------------+
| **Reverse proxy**     | *Application*         |  NGINX                    |
+-----------------------+-----------------------+---------------------------+
| **Backend**           | *Language*            |  Python                   |
+                       +-----------------------+---------------------------+
|                       | *Framework*           |  Django                   |
+                       +-----------------------+---------------------------+
|                       | *API*                 |  Django REST framework    |
+                       +-----------------------+---------------------------+
|                       | *WebSockets*          |  Django Channels          |
+                       +-----------------------+---------------------------+
|                       | *OAuth2 provider*     |  django-oauth-toolkit     |
+                       +-----------------------+---------------------------+
|                       | *Search*              |  django-elasticsearch-dsl |
+                       +-----------------------+---------------------------+
|                       | *WSGI server*         |  Gunicorn                 |
+                       +-----------------------+---------------------------+
|                       | *ASGI server*         |  Daphne                   |
+-----------------------+-----------------------+---------------------------+
| **Frontend**          | *Language*            |  JavaScript               |
+                       +-----------------------+---------------------------+
|                       | *Framework*           |  React                    |
+                       +-----------------------+---------------------------+
|                       | *State*               |  Redux                    |
+                       +-----------------------+---------------------------+
|                       | *Components*          |  Semantic UI React        |
+                       +-----------------------+---------------------------+
|                       | *Transpiler*          |  Babel                    |
+                       +-----------------------+---------------------------+
|                       | *Bundler*             |  Webpack                  |
+-----------------------+-----------------------+---------------------------+

- Tier I (no dependencies on other infrastructure)

  - Message broker
  - Channel layer
  - Session store
  - Communication store
  - Verification store
  - Application store
  - Database
  - Cache

- Tier II (started after Tier I)

  - Intranet server
  - Internet server

- Tier III (started after Tier II)

  - Reverse proxy

The tiers describe the order in which Docker Compose starts the containers, not the order in which they become usable.
Nothing waits on a health check, so a container in a higher tier can be up and running before the ones below it are ready to answer.

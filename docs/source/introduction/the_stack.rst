The stack
=========

Unless otherwise specified, Omniport runs on the latest versions of all the 
components in the stack. This means that there is no LTS version or long-term
release and Omniport is always a rolling distribution.

+-----------------------+-----------------------+-----------------------+
| Sphere                | Sub-sphere            |  Technology           |
+=======================+=======================+=======================+
| **Orchestration**     | *Containers*          |  Docker               |
+-----------------------+-----------------------+-----------------------+
| **NoSQL databases**   | *Sessions*            |  Redis                |
+                       +-----------------------+-----------------------+
|                       | *Communications*      |  Redis                |
+                       +-----------------------+-----------------------+
|                       | *Channels*            |  Redis                |
+                       +-----------------------+-----------------------+
|                       | *Temporary app*       |  Redis                |
+                       +-----------------------+-----------------------+
|                       | *GUI*                 |  Redis Commander      |
+-----------------------+-----------------------+-----------------------+
| **SQL database**      | *Application*         |  PostgreSQL           |
+                       +-----------------------+-----------------------+
|                       | *Library*             |  Psycopg2             |
+-----------------------+-----------------------+-----------------------+
| **Cache**             | *Application*         |  Memcached            |
+-----------------------+-----------------------+-----------------------+
| **Message broker**    | *Application*         |  RabbitMQ             |
+                       +-----------------------+-----------------------+
|                       | *Library*             |  Celery               |
+-----------------------+-----------------------+-----------------------+
| **Reverse proxy**     | *Application*         |  NGINX                |
+-----------------------+-----------------------+-----------------------+
| **Backend**           | *Language*            |  Python               |
+                       +-----------------------+-----------------------+
|                       | *Framework*           |  Django               |
+                       +-----------------------+-----------------------+
|                       | *WSGI server*         |  Gunicorn             |
+                       +-----------------------+-----------------------+
|                       | *ASGI server*         |  Daphne               |
+-----------------------+-----------------------+-----------------------+
| **Frontend**          | *Language*            |  JavaScript           |
+                       +-----------------------+-----------------------+
|                       | *Framework*           |  React                |
+                       +-----------------------+-----------------------+
|                       | *Transpiler*          |  Babel                |
+                       +-----------------------+-----------------------+
|                       | *Bundler*             |  Webpack              |
+-----------------------+-----------------------+-----------------------+

- Tier I (no dependencies on other infrastructure)

  - Message broker
  - Channel layer
  - Session store
  - Notification store
  - Application store
  - Database
  - Cache

- Tier II (depend on and wait for Tier I to be ready)

  - Intranet server
  - Internet server
  - Redis GUI

- Tier III (depend on and wait for Tier II to be ready)

  - Reverse proxy

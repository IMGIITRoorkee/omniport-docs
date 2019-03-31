Logs
====

This script starts the Bash container needed for examining the logs generated
by various services in production.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/start/logs.sh

This will drop you into a familiar but foreign Bash shell. Executing ``ls`` here
reveals the log directories.

.. code-block:: console

  # ls
  reverse_proxy_logs
  web_server_logs
  ...

The ``web_server_logs`` directory further contains three directories.

.. code-block:: console

  # cd web_server_logs
  # ls
  daphne_logs
  gunicorn_logs
  supervisord_logs
  ...

All these directories contains various logs that can be examined. The container
also supports the ``tail`` binary fortunately enabling you to tail and detect
errors.

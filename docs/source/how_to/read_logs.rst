... read logs?
==============

Reading Omniport logs is just as easy as writing them is. That's largely because
a lot of the work has been done for you out-of-the-box. We're really generous 
that way.

Enter logs container
--------------------

From the Omniport Docker root directory, run the script that opens a shell into
the logging volumes.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/start/logs.sh

This will drop you into the Docker shell. For more on this script, you can read
the :doc:`script article <../references/scripts/docker/start/logs>`.

Find the log directory
----------------------

An assortment of events are continuously logged in Omniport. A list of these
events and their corresponding log locations are mentioned here.

Reverse proxy logs
++++++++++++++++++

:Directory:
  /reverse_proxy_logs/

NGINX
.....

:Subdirectory:
  nginx_logs/

The following is a map of the sources and log files for NGINX. 

+---------------------+---------------------+
| Source              | Log file            |
+=====================+=====================+
| Intranet access log | intranet-access.log |
+---------------------+---------------------+
| Intranet error log  | intranet-error.log  |
+---------------------+---------------------+
| Internet access log | internet-access.log |
+---------------------+---------------------+
| Internet error log  | internet-error.log  |
+---------------------+---------------------+

Web server logs
+++++++++++++++

:Directory:
  /web_server_logs/

Gunicorn
........

:Subdirectory:
  gunicorn_logs/

The following is a map of the sources and log files for Gunicorn. 

+----------------------+----------------+
| Source               | Log file       |
+======================+================+
| Access log           | <x>-access.log |
+----------------------+----------------+
| Error log            | <x>-error.log  |
+----------------------+----------------+
| Django log           | <x>-django.log |
+----------------------+----------------+
| Service and app logs | <x>-<name>.log |
+----------------------+----------------+

Here <x> must be replaced with **1** or **2** based on the site IDs. For more 
information on site IDs, refer to the :doc:`site-level configuration docs
<../references/config_files/project/site_yml>`.

Also <name> should be the actual name (not verbose name) of the service or app 
in question.

Daphne
......

:Subdirectory:
  daphne_logs/

The following is a map of the sources and log files for Daphne. This is not 
exhaustive because Daphne is used exclusively on ``ws/`` URLs and is not 
well-documented itself.

+----------------------+----------------+
| Source               | Log file       |
+======================+================+
| Access log           | <x>-access.log |
+----------------------+----------------+

Here <x> must be replaced with **1** or **2** based on the site IDs. For more 
information on site IDs, refer to the :doc:`site-level configuration docs
<../references/config_files/project/site_yml>`.

Supervisor
..........

:Subdirectory:
  supervisord_logs/

The following is a map of the sources and log files for Supervisor. 

+-----------------+-------------------------+
| Source          | Log file                |
+=================+=========================+
| Self            | self-<x>.log            |
+-----------------+-------------------------+
| Gunicorn stdout | gunicorn-<x>-stdout.log |
+-----------------+-------------------------+
| Gunicorn stderr | gunicorn-<x>-stderr.log |
+-----------------+-------------------------+
| Daphne stdout   | daphne-<x>-stdout.log   |
+-----------------+-------------------------+
| Daphne stderr   | daphne-<x>-stderr.log   |
+-----------------+-------------------------+

Here <x> must be replaced with **1** or **2** based on the site IDs. For more 
information on site IDs, refer to the :doc:`site-level configuration docs
<../references/config_files/project/site_yml>`.

Tail the log
------------

For real-time monitoring we go back to the classic ``tail`` utility whose 
capabilities have withstood the test of time.

.. code-block:: console

  docker@logs:/<logs_directory>$ tail -n <line_count> -f <log_file_name>

And there you have it. You are now armed with a comprehensive understanding of
where to find logs to troubleshoot any and every error that could hit Omniport.
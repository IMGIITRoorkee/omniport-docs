... write logs?
===============

A developer's got to write logs. When things break down, when errors pop up and 
when something is off, we refer to logs to comprehend what's happening.

But for there to be logs, one needs to write logging in one's app. Here's how
to do just that.

Getting a logger
----------------

To write logs, start by getting a logger instance. This can be achieved in one
line of code. 

.. code-block:: python

  import logging
  
  logger = logging.getLogger(__name__)

The value of ``__name__`` here is a dot separate path upto the current file. In
a file named ``hello.py`` inside the module ``views`` inside the app 
``application``, it's value is ``application.views.hello``.

Omniport has been configured to automatically configure loggers and handlers via
Discovery. Each discovered app has a dedicated logger, configured to work with 
two handlers: ``console`` (only active during development and debugging) and one 
named after the app (only active in production).

The latter of the two writes logs to file, rotated every midnight keeping the 
last 32 days (nearly a month, except 32 = 2\ :sup:`5` which is a cool number).

Back to the point, all of it happens in the background, like magic, so there's 
very little to do on your part.

.. warning::

  The logger Discovery registers is named after the ``name`` in your app's
  ``config.yml``, not after the directory your app sits in. ``__name__`` is
  rooted at the directory. When the two agree, which is the case for any app
  made from the template, everything below follows and you need read no
  further. When they differ, your records find no configured ancestor, fall
  through to an unconfigured root logger, and anything below ``WARNING``
  vanishes without an error. If your logs are missing, compare the two names
  before looking anywhere else.

Where your logs end up
----------------------

Log files are named after the server that wrote them, the site they were
written for, and your app.

::

  /web_server_logs/<server>_logs/<site_id>-<app>.log

``<app>`` is the ``name`` from your ``config.yml``.
``<site_id>`` is the ``id`` of the site, which is 1 for the intranet site and 2
for the Internet site.
``<server>`` is ``gunicorn`` or ``daphne``, whichever handled the request, so a
line written while serving a WebSocket lands in a different directory from one
written while serving HTTP.

In development neither server is running, and your logs collect in
``server_logs/`` instead. Background tasks land there too, whatever the
environment, because a worker is not a server and names none.

.. seealso::

  For the full map of log directories, see :doc:`how to read logs <read_logs>`.

Writing logs
------------

Writing logs is easy as well.

.. code-block:: python

  logger.critical('This is a critical message!!')
  logger.error('This is an error message!')

  logger.warning('This is a warning message')
  logger.info('This is an info message')
  
  logger.debug('This is a debug message that no handler will catch')

Both handlers, and the logger itself, are pinned to ``INFO``. Anything you send
to ``debug`` is discarded before a handler ever sees it, in development as well
as in production, and there is no setting that turns it back on. Log at ``info``
anything you would want to read later.

Two more loggers exist that are worth knowing about, neither of them yours.
``core`` carries the portal's own account of what it did, and
``kernel_permissions`` records every check of the ``alohomora``,
``helpcentre``, ``omnipotence`` and ``polyjuice`` permissions, naming the user
and saying whether the permission was granted. If your app gates on one of
those, the record of who was let in and who was refused is in that file rather
than in yours, and it is never written to the console.

That's practically all there is to it.
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

Writing logs
------------

Writing logs is easy as well.

.. code-block:: python

  logger.critical('This is a critical message!!')
  logger.error('This is an error message!')

  logger.warning('This is a warning message')
  logger.info('This is an info message')
  
  logger.debug('This is a debug message that no handler will catch')

That's practically all there is to it.
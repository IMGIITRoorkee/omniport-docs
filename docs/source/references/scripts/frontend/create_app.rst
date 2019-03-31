Create app
==========

.. note::

  Make sure you have the corresponding backend ready before you start the
  frontend to avoid any nasty surprises.

Although creating a new app on ``omniport-frontend`` is really easy, the main
reason being that the process of creating one and the file structure are both
pretty much identical to a normal React app, we have provided a convenient
method to make this process effortless for the developer.

Usage
-----

.. code-block:: console

  [dev omniport-frontend]$ ./scripts/create/app.sh
  
You are asked for the name of your app that you have to provide in lower case
letters, separating words with spaces. For example, for an app named 'Placement
and internship' you must enter

.. code-block:: text

  placement and internship

That's about it! It clones a pre-defined `template from GitHub
<https://github.com/IMGIITRoorkee/omniport-frontend-template/>`_, makes
necessary replacements with the app name you have provided and creates a new
folder in the ``omniport/apps/`` folder.

Restarting the server will make Discovery aware of your new project. The
root URL of your newly created app can be deduced by replacing spaces in the
app name you provided with underscores, ``_``. This is, needless to say, 
customisable via the ``config.json`` file.

You should be greeted with a pleasant homepage.
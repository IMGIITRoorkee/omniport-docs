Create app
==========

.. note::

  After you have an up and running API make sure to create a React app for the
  frontend of the project.

Although creating a new app on ``omniport-backend`` is really easy, the main
reason being that the process of creating one and the file structure are both
pretty much identical to a normal Django app, we have provided a convenient
method to make this process effortless for the developer.

Usage
-----

.. code-block:: console

  [dev omniport-backend]$ ./scripts/create/app.sh
  
You are asked for the name of your app that you have to provide in lower case
letters, separating words with spaces. For example, for an app named 'Placement
and internship' you must enter

.. code-block:: text

  placement and internship

That's about it! It clones a pre-defined `template from GitHub
<https://github.com/IMGIITRoorkee/omniport-app-template/>`_, makes
necessary replacements with the app name you have provided and creates a new
folder in the ``omniport/apps/`` folder.

Restarting the server will make Discovery aware of your new project. The
root URL of your newly created API can be deduced by replacing spaces in the
app name you provided with underscores, ``_``. This is, needless to say, 
customisable via the ``config.yml`` file.

You should be greeted with a JSON API, greeting you on your success.

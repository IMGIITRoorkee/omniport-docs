Omniport Docs
=============

.. note::

  You must have ``Python 3.8`` and ``pipenv`` installed before you can set
  up the documentation locally.

#. Install the project dependencies.

    .. code-block:: console
   
        $ pipenv install --skip-lock

   Omit the flag ``--skip-lock`` if you want the latest packages. Keep in mind
   that the project has been tested on the versions of the packages specified
   in the ``Pipfile.lock`` so its compatibilty with the latest packages might
   not be assured. 

#. Start the ``pipenv`` virtual environment via running the following command.
   Or you can prefix the commands for starting the server or for building docs
   using ``pipenv run``.

    .. code-block:: console

        $ pipenv shell

#. To start the development server, run the following commands inside ``/docs``.
   This will automatically re-build your changes as you make them.

    .. code-block:: console

       $ make dev

   Pass extra flags like port (default: 8000) by suffixing
   ``SPHINXDEVOPTS="-p 8080"`` with the above command.

#. Build the documentation into HTML pages by running the following command
   inside ``/docs``.

    .. code-block:: console

       $ make html

   This will create the ``docs/build`` directory. You can preview it using one
   of Python's module called ``http.server``.

#. To build the documentation into some other format, refer to ``make help``
   command for all the options available.

Cannot start the virtual environment?
-------------------------------------

If you keep getting the following error when you try to run ``pipenv shell``:

.. code-block:: none

    Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.
    No action taken to avoid nested environments.

Run ``exit`` to resolve the issue. You will be able to start the virtual
environment now.

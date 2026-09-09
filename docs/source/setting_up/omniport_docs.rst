Omniport Docs
=============

.. note::

  You must have ``pipenv`` installed before you can set up the documentation
  locally. The pinned dependencies are old enough to constrain the interpreter:
  they install on Python 3.8, which is what the published build uses, and on
  anything up to 3.11, but not beyond it.

#. Install the project dependencies.

    .. code-block:: console
   
        $ pipenv install

   This installs the versions pinned in ``Pipfile.lock``, which are the ones
   the project has been tested on and the ones the published documentation is
   built from. Adding ``--skip-lock`` does the opposite, ignoring the lock file
   and resolving the latest release of each package instead, so compatibility
   is then not assured. Recent releases of ``pipenv`` have removed that flag
   altogether.

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

   This writes the pages into ``docs/build/html``. Serve that directory, not
   ``docs/build``, with Python's ``http.server`` module to preview them.

    .. code-block:: console

       $ python -m http.server --directory build/html

#. To build the documentation into some other format, refer to ``make help``
   command for all the options available.

Where the published documentation comes from
--------------------------------------------

Merging to ``master`` publishes the documentation. The build installs
``requirements.txt``, which holds what Sphinx needs and nothing else. The live
reload tooling lives in ``requirements-dev.txt``, which pulls the build set in,
so install that one if you are editing rather than only building.

Both are maintained by hand alongside ``Pipfile.lock`` and nothing keeps them in
step, so a dependency change has to be made in both places or the published
build will differ from the one you tested locally.

Cannot start the virtual environment?
-------------------------------------

If you keep getting the following error when you try to run ``pipenv shell``:

.. code-block:: none

    Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.
    No action taken to avoid nested environments.

Run ``exit`` to resolve the issue. You will be able to start the virtual
environment now.

## Setup

#### Prerequisites

- `Python 3.7`
- `pipenv` (Install by running `$ pip install pipenv`)

#### Instructions

1. Install the project dependencies.
   ```sh
   $ pipenv install
   ```
   Add the flag `--skip-lock` if you do not want the latest packages and prevent
   the dependencies from upgrading themselves.

2. Start the `pipenv` virtual environment via running the following command. Or
   you can prefix the commands for starting the server or building using
   `pipenv run`.
   ```sh
   $ pipenv shell
   ```

3. To start the development server, run the following commands inside `/docs`.
   This will automatically re-build your changes as you make them.
   ```sh
   $ sphinx-autobuild source build -p <port number (default 8000)>
   ```

4. Build the documentation into HTML pages by running the following command
   inside `/docs`.
   ```sh
   $ make html
   ```
   This will create the `docs/build` directory. You can preview it using one of
   Python's module called `http.server`.

5. To build the documentation into some other format, refer to `make help`
   command for all the options available.

#### Cannot start the virtual environment?

If you keep getting the following error when you try to run `pipenv shell`
```
Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.
No action taken to avoid nested environments.
```
Run `exit` to resolve the issue. You will be able to start the virtual
environment now.

:sourcefiles:
  omniport-backend/omniport/core/configuration/models/app/app.py
  omniport-backend/scripts/create/app.sh
  omniport-frontend/scripts/create/app.sh

... create an app?
==================

Backend
-------

File structure of a typical app is as follows.

::

  placement_and_internship
  ├── config.yml
  ├── LICENSE
  ├── README.md
  ├── __init__.py
  ├── http_urls.py
  ├── apps.py
  ├── migrations
  │   └── __init__.py
  ├── models
  │   └── __init__.py
  ├── static
  │   └── assets
  │       ├── favicon.ico
  │       ├── icon.svg
  │       ├── logo.svg
  │       └── README.md
  └── views
      ├── hello_world.py
      └── __init__.py

Look familiar? That's because it is. The structure of the app is the same, with
a few notable exceptions as below.

``config.yml``
++++++++++++++

We need to create, or if it exists, populate the ``config.yml`` file with the 
internal name, the display name, the URLs and the acceptables as shown in the 
example.

.. code-block:: yaml

  nomenclature:
    name: placement_and_internship
    verboseName: Placement and internship
  description: Build your resume, apply and get placed
  baseUrls:
    http: placement_and_internship/
    static: placement_and_internship/
  isApi: true
  acceptables:
    ipAddressRings:
    - self
    - specifics
    - maintainers
    - intranet
    roles:
    - name: Student
      activeStatuses:
      - IS_ACTIVE

.. warning::

  ``http:`` under ``baseUrls:`` is not optional, even for an app that serves no
  HTTP of its own. Omniport reads it for every installed app on every request
  and does not check whether it is there, so leaving it out takes down every
  page of the portal rather than just yours. The same applies to ``static:`` as
  soon as your app ships a ``static/`` folder, which the example above does.

An app that raises notifications or files things under categories may also
declare a ``categorisation:`` list, giving the tree of categories it wants
created under its own name. Leave it out if your app has no such tree.

.. seealso::

  For more information on ``config.yml`` see :doc:`this
  <../references/config_files/app/config_yml>`.

``http_urls.py``
++++++++++++++++

This file is the same old ``urls.py`` of Django, with the name changed in order
to differentiate if from the ``ws_urls.py`` file that configures the URLconf 
for WebSockets. 

``ws_urls.py``
++++++++++++++

This file is the URLconf for Django Channels that guides requests from 
WebSockets. This file needs to exist if your app makes use of realtime 
communications. If you define ``ws:`` in your ``baseUrls:`` you must have this 
file in your app's root folder.

The two go together in both directions. Declaring ``ws:`` without the file
stops the whole portal from loading its URLs, and shipping the file without
declaring ``ws:`` means it is never imported and your consumers never run.

``static/assets/``
++++++++++++++++++

This folder, with no variations in the directory names, contains various app
assets such as icon, favicon and logo. The names are fixed too. Omniport looks
for ``favicon``, ``icon`` and ``logo``, taking the favicon as ``.ico`` only and
the other two as ``.svg``, ``.png`` or ``.jpg``, preferring them in that order.
A file under any other name is ignored, and one that is absent falls back to
the portal's own imagery rather than failing.

Frontend
--------

File structure of a typical app is as follows.

::

  placement_and_internship
  ├── config.json
  ├── LICENSE
  ├── README.md
  └── src
      ├── components
      │   └── app.js
      ├── css
      │   └── app.css
      ├── index.js
      ├── reducers
      │   ├── exampleReducer.js
      │   └── index.js
      └── urls.js

Look familiar? That's because it is. The structure of the app is the same, with
a few notable exceptions as below.

``config.json``
+++++++++++++++

We need to create, or if it exists, populate the ``config.json`` file with the 
internal name, the display name and the URLs as shown in the example.

.. code-block:: json

  {
    "nomenclature": {
      "name": "placement_and_internship",
      "verboseName": "Placement and Internship"
    },
    "baseUrl": "/placement_and_internship",
    "source": "placement_and_internship/src/index"
  }

.. seealso::

  For more information on ``config.json`` see :doc:`this
  <../references/config_files/app/config_json>`.

``index.js``
++++++++++++

``index.js`` plays an important role in connecting your app to ``Omniport``. It
act as a gateway between ``omniport-core`` and your app.

An ``index.js`` file looks like this.

.. code-block:: jsx

  import React, { Component } from 'react'
  import { Route } from 'react-router-dom'
  import App from './components/app'
  import { createStore, applyMiddleware } from 'redux'
  import { Provider } from 'react-redux'
  import thunk from 'redux-thunk'

  import rootReducers from './reducers'

  export default class AppRouter extends Component {
    constructor (props) {
      super(props)
      this.store = createStore(rootReducers, applyMiddleware(thunk))
    }

    render () {
      const { match } = this.props
      return (
        <Provider store={this.store}>
          <Route path={`${match.path}/`} component={App} />
        </Provider>
      )
    }
  }

Here ``App`` is the normal react app component from which you can proceed
similar to a normal react app.

``urls.js``
+++++++++++

``urls.js`` contains both navigation URLs for frontend as well as API endpoints
for backend.

An example of ``urls.js`` can be as follows.

.. code-block:: jsx

  import appConfig from '../config.json'

  // Frontend URLs
  export function urlBaseView () {
    return `${appConfig.baseUrl}`
  }

  export function urlGroupDetailView (slug) {
    return `${urlBaseView()}/${slug}`
  }

  export function urlGroupTeam (slug) {
    return `${urlGroupDetailView(slug)}/team`
  }

  // Backend URLs
  export function urlBase () {
    return `/api/groups/`
  }

  export function urlGroupList () {
    return `${urlBase()}group/`
  }

  export function urlActiveGroupPost () {
    return `${urlBase()}post/`
  }

Before your app appears
-----------------------

A finished app directory is not yet an installed app. Four things stand between
the two.

- **Put each half where its codebase looks for it.**

  The backend app belongs in ``omniport/apps/`` inside ``omniport-backend``, and
  the frontend app in ``omniport/apps/`` inside ``omniport-frontend``. Those two
  folders are the only places that are scanned.

- **Name the directory after the app.**

  The directory name must be the same string as the ``name`` in ``config.yml``.
  When the two differ, the app cannot find its own configuration and Django
  stops at startup.

- **Have the app allowed on the site.**

  Being discovered is not the same as being served. Unless the site allows
  every app, your app's ``name`` must be added to the list of allowed apps in
  that site's configuration file. Until it is, the app is given no URLs at all,
  so its API answers 404 and it never appears in the portal. This is the step
  most often missed, and it is the sysadmin's to take, not yours.

  .. seealso::

    The list lives under ``allowances:`` in :doc:`the site configuration file
    <../references/config_files/project/site_yml>`.

- **Restart the backend, rebuild the frontend.**

  Discovery runs once, while Django starts, so the container has to be
  restarted before it sees a new app. The frontend regenerates its own registry
  as part of building, so a rebuild is enough there, though a development
  server already running will not notice.

Then migrate your app if it defines any models. ``makemigrations`` takes the
app's ``name`` rather than its directory.

Automate all of this
--------------------

.. note::
  
  Even if it's too complicated for you, refer to the ``create/app.sh`` scripts
  provided by Omniport for both the 
  :doc:`backend <../references/scripts/backend/create_app>`
  and the
  :doc:`frontend <../references/scripts/frontend/create_app>`.

  Profit.

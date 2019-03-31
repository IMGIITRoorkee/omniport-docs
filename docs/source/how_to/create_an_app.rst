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

We need to create, or if it exists, populate the ``config.json`` file with the 
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

``static/assets/``
++++++++++++++++++

This folder, with no variations in the directory names, contains various app
assets such as icon, favicon and logo.

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

Automate all of this
--------------------

.. note::
  
  Even if it's too complicated for you, refer to the ``create/app.sh`` scripts
  provided by Omniport for both the 
  :doc:`backend <../references/scripts/backend/create_app>`
  and the
  :doc:`frontend <../references/scripts/frontend/create_app>`.

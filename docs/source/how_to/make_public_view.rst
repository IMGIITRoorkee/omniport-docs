... make a public view for an app?
==================================

To make a part of an application visible to the user without logging in Omniport we can follow the following steps -

.. note::

  Only apps can have a public view.
  A ``public`` key in a service's ``config.json`` is read by nothing.

First we need to add a ``public`` key in the ``config.json`` of the app with the source file for the routes of public view. Preferably, we name this file as ``public.js``.

.. code-block:: json

    "public": {
        "source": "student_profile/src/public",
        "baseUrl": "/student_profile"
    }

The view is then served under ``/public``, ahead of the ``baseUrl`` you gave it.
An app declaring the block above is reached at ``/public/student_profile`` and not at ``/student_profile``, so give ``baseUrl`` a leading slash, since the two are joined as they are written.

Then we edit the ``public.js`` file and we try to keep it like the ``index.js`` file, containing the routes of the public views.

.. code-block:: javascript

  import React, { Component } from "react";
  import { createStore, applyMiddleware, compose } from "redux";
  import { Provider } from "react-redux";
  import thunk from "redux-thunk";
  import { BrowserRouter as Router, Route } from "react-router-dom";

  import rootReducers from "./reducers";
  //local imports which are meant to be open for public-view
  import App from "./App";
  //css files can be same as of index.js
  import "./index.css";

  export default class AppRouter extends Component {
    constructor(props) {
      super(props);
      const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
      this.store = createStore(rootReducers, composeEnhancers(applyMiddleware(thunk)));
    }
    render() {
      const { match } = this.props;
      return (
        <Provider store={this.store}>
          <Router>
            {/*
              Add the routes that are meant to be open for public-view,
              and import the corresponding components. An example is below.
            */}
            <Route path={`${match.path}`} component={App} />
          </Router>
        </Provider>
      );
    }
  }

In order to view the ``app-header`` from formula-one we need to change the mode of the app-header as ``public`` when we call the component in our app.
Pass ``userDropdown={false}`` alongside it, which is what replaces the user menu with a log in button for a visitor who has no session.

Opening the route is not enough
-------------------------------

A public route changes the frontend and nothing else.
Every view in Omniport requires an authenticated user unless it says otherwise, so a public page pointed at an ordinary app renders its shell and then fails every request it makes for data.

There is no key in ``config.yml`` that changes this.
Each endpoint the public page reads has to say so for itself.

.. code-block:: python

  from rest_framework.permissions import AllowAny

  class StudentSearchList(generics.ListAPIView):
      permission_classes = (AllowAny, )

.. warning::

  Say ``AllowAny`` rather than leaving ``permission_classes`` empty.
  An empty list has the same effect today, but it reads as an oversight rather
  than a decision, and it is indistinguishable from the mistake of forgetting
  the attribute on a view that was never meant to be public.

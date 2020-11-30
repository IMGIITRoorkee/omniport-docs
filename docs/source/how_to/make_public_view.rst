... make a public view for an app?
==================================

To make a part of an application visible to the user without logging in omniport we can follow the following steps -

First we need to add a ``public`` key in the ``config.json`` of the app with the source file for the routes of public view. Preferably, we name this file as ``public.js``.

.. code-block:: json

    "public": {
        "source": "student_profile/src/public",
        "baseUrl": "/student_profile"
    }

Then we edit the ``public.js`` file and we try to keep it like the index.js file, containing the routes of the public-views.

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
                        /*
                            Add the routes that are meant to be open for public-view,
                            and import the corresponding components. An example is shown below -
                        */
                        <Route path={`${match.path}`} component={App} />
                    </Router>
                </Provider>
            );
        }
    }

In order to view the ``app-header`` from formula-one we need to change the mode of the app-header as ``public`` when we call the component in our app.
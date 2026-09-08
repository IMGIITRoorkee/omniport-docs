... use Omniport OAuth2?
========================

The following walkthrough will show you how to integrate Omniport OAuth2 in 
your applications.

Registering your application
----------------------------

Register your app for Omniport OAuth2 by visiting the developer portal on
``/developer/add``. Here you will be asked a few details about your app. You
have to

- add your app name, redirect URIs in correct format. 
- describe your app in strictly 127 - 511 words. 
- select the minimum number of scopes (user information) that you will require 
  for your app. 
- read 
  :doc:`Omniport developer terms of use <../legal/developer_terms_of_use/>` and
  agree to all of the terms therein.

Click on Add button to proceed. You will be taken to app administration 
dashboard. Here you can edit a few things about your app, like branding, team
members and redirect URIs.

Note down your **client ID** and **client secret key** from the dashboard.

.. note::
  
  Describe your app adequately and truthfuly. Also keep in mind that selecting
  as fewer scopes as possible will increase the odds in favour of approval of
  your app by the administration. After submitting your app request, your
  approval status can be seen and tracked from the developer dashboard.

.. warning::
  You will be unable to use OAuth2 without said approval. Users will not be able
  to access your authorise your app to use their data.

Authorising the user
--------------------

To authorise your users, redirect them to ``/oauth/authorise`` through a ``GET`` 
request with the following parameters.

============================== ================================================================
Parameter                       Description
============================== ================================================================
**client_id** (required)        The client ID you obtained from the dashboard
**response_type** (required)    ``code`` as it is, this being the only supported flow
**redirect_uri**                One of the redirect URIs you have registered on the dashboard
**scope**                       ``read write``, which is what the consent screen submits
**state**                       Any string you want the ``REDIRECT_URI`` to receive on success
============================== ================================================================

.. warning::

  If the ``redirect_uri`` does not match any of the listed redirect URIs, the 
  authorisation request will fail and the user will not see an authorisation 
  screen.

.. note::

  For additional information on the query parameters refer to the
  `documentation <https://django-oauth-toolkit.readthedocs.io/en/latest/>`_ of
  the Django OAuth Toolkit PyPI package.

.. note::

  ``/oauth`` and ``/open_auth`` are two different things and it is worth
  keeping them apart. ``/oauth`` is a page in the browser, where the user sees
  and answers the consent screen. ``/open_auth`` is the API your server calls.
  You send users to the first and your application talks to the second.

A sample authorisation request URL could therefore look like the one below.

::

  /oauth/authorise/?client_id=MY_CLIENT_ID
    &response_type=code
    <&redirect_uri=REDIRECT_URI>
    <&state=RANDOM_STATE_STRING>

The user experience
-------------------

At this point, you’ve forwarded the user to Omniport authorisation page, where
they will be greeted by the following screen (they might need to log in before
they see it).

.. image:: /_static/gif/oauth.gif
  :target: /
  :align: center
  :alt: OAuth authorisation screen

Neither you or your application can or need to do anything here; Omniport
deals with the user, receiving the user's intent to approve or disapprove your 
app. Based on whether the user approves the app or denies it, the user will be 
redirected to ``REDIRECT_URI`` or back to Omniport home.

Handling the Response from Omniport OAuth2
------------------------------------------

If the user clicks approves the app to access their data on the previous screen, 
OAuth2 will redirect the user to the ``REDIRECT_URI`` specified earlier with a code 
parameter, any state passed to the authorisation URL will be forwarded to 
``REDIRECT_URI``.

::
  
  REDIRECT_URI?code=AUTHORISATION_CODE
    <&state=RANDOM_STATE_STRING>

This one-time authorisation code has a TTL of 1 minute. So the next step, which
is anyways supposed to be automatic must be done pretty fast.

Getting the access and refresh token
------------------------------------

Once your application has an authorization
code, it will now need to exchange the authorization code for a pair of access
and refresh tokens from Omniport.

To get these tokens, you’ll need to make a ``POST`` request to 
``/open_auth/token/`` with the following parameters:

============================= ===============================================================
Parameter                      Description
============================= ===============================================================
**client_id** (required)       The client ID you obtained from the dashboard
**client_secret** (required)   The client secret you obtained from the dashboard
**grant_type** (required)      ``authorization_code`` as it is
**redirect_uri** (required)    One of the redirect URIs you have registered on the dashboard
**code** (required)            The authorisation code sent to the REDIRECT_URI
============================= ===============================================================

If everything goes right and the request is successful, you’ll receive a 200
response containing a ``JSON`` body like this: 

.. code-block:: json

  {
    "access_token": "vqygrcouTuyAYHZLz3rGcZf5FpPd3K",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "BbVJsFL1Ks5LkXDe9ZFUIFvIzXKt9M"
  }

However, if the response is not successful, you’ll receive an error response.

.. code-block:: json

  {
    "error": "some_error_message"
  }

Using the access token
----------------------

Now that you have the access token, you can get the user data by sending a
``GET`` request to ``/open_auth/get_user_data/`` with the access token in the
header as follows:

.. code-block:: json

  {
    "Authorization": "Bearer vqygrcouTuyAYHZLz3rGcZf5FpPd3K"
  }

where ``vqygrcouTuyAYHZLz3rGcZf5FpPd3K`` is the access token.

If the access token is valid, then you will receive a 200 response
with a dictionary containing the user's information based on the scopes
of the client app, similar to this:

.. code-block:: json

    {
       "userId": 1234,
       "username": "15xxx009",
       "person": {
          "shortName": "dhruvkb",
          "fullName": "Dhruv Kanti Bhanushali",
          "roles": [
             {
                "role": "Student",
                "activeStatus": "ActiveStatus.IS_ACTIVE"
             },
             {
                "role": "Maintainer",
                "activeStatus": "ActiveStatus.IS_ACTIVE"
             }
          ]
       },
       "student": {
            "enrolmentNumber": "15xxx009"
       },
       "contactInformation": {
            "instituteWebmailAddress": "xyz@iitr.ac.in"
       }
    }

Each object carries more fields than are shown here, and which of them you
receive depends on the scopes your application holds. Read the fields you need
by name and ignore the rest, rather than assuming the shape above is complete.

However, if the access token is missing, expired or revoked, you will receive
a ``401 Unauthorized`` response.

.. code-block:: json

    {
        "detail": "Authentication credentials were not provided."
    }

.. code-block:: json

    {
        "detail": "Invalid token header. No credentials provided."
    }

The first is returned when no ``Authorization`` header was sent, the second when
one was sent but the token in it is not valid. Treat both the same way, by
sending the user through the flow again.

Generating new access token using refresh token
-----------------------------------------------

The access token has a short lifetime of **36000 seconds**. If it expires, you'll need to generate new 
tokens either by re-authenticating the user or using the refresh token.

To generate these new tokens, you’ll need to make a ``POST`` request to 
``/open_auth/token/`` with the following parameters:

============================= ===============================================================
Parameter                      Description
============================= ===============================================================
**client_id** (required)       The client ID you obtained from the dashboard
**client_secret** (required)   The client secret you obtained from the dashboard
**grant_type** (required)      ``refresh_token`` as it is
**refresh_token** (required)   The refresh token received in exchange of authorization code.
============================= ===============================================================

The newly created tokens were successfully generated if you get a 200 response. The "JSON" response body will appear as follows:

.. code-block:: json

  {
    "access_token": "cjlgnpwhfuyAYHZLz3rGcZf5FpPd3K",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "NhdwsFL1Ks5LkXDe9ZFUIFvIzXKt9M"
  }

You will get an error response, though, if the response is unsuccessful.

.. code-block:: json

  {
    "error": "some_error_message"
  }

Logging out the user
--------------------

You can revoke the tokens to bar access when the user logs out.

To revoke the access and refresh token,  you’ll need to make a ``POST`` request to ``/open_auth/revoke_token/`` 
with the following parameters:

============================== ===============================================================
Parameter                      Description
============================== ===============================================================
**client_id** (required)       The client ID you obtained from the dashboard
**client_secret** (required)   The client secret you obtained from the dashboard
**token** (required)           The access/refresh token you wish to revoke
**token_type_hint** (required) ``access_token`` or ``refresh_token``
============================== ===============================================================

Handling errors
---------------

Every endpoint below ``/open_auth/`` answers with a status code that says what
your application should do next. Read the code before the body, and never treat
a failed request as the endpoint being down.

============ ============================= ===============================================
Status        Meaning                       What to do
============ ============================= ===============================================
``400``       The request was rejected      Read ``error`` in the body, see the table below
``401``       The token is not usable       Send the user through the flow again
``403``       The application is not        Wait for approval, no request will succeed
              approved                      until it is granted
``404``       No such approved application  Check the client ID, and that the app is
                                            approved
``429``       Too many requests             Wait, then retry, see rate limits below
``500``       Omniport failed               Retry once, then report it to us
============ ============================= ===============================================

A rejected request carries an ``error`` from the OAuth2 specification.

.. code-block:: json

  {
    "error": "invalid_grant"
  }

========================== =====================================================
Error                       Cause
========================== =====================================================
``invalid_request``         A required parameter is missing or repeated
``invalid_client``          The client ID or secret is wrong
``invalid_grant``           The code has expired, been used already, or was
                            issued to a different client or redirect URI
``unsupported_grant_type``  The ``grant_type`` is not one this server supports
``invalid_scope``           The scope requested exceeds what the application
                            holds
========================== =====================================================

.. warning::

  ``invalid_grant`` is the one integrators most often mishandle. Authorisation
  codes are valid for sixty seconds and may be exchanged exactly once, so a
  retry that replays the same code always fails. Send the user through the flow
  again to obtain a fresh code, rather than retrying the exchange.

Rate limits
-----------

Omniport limits how fast an application may call these endpoints. The limits are
counted per application, not per user, so how many people use your application
does not change how much of the limit each of them gets.

======================================= ==================================================
Limit                                    Applies to
======================================= ==================================================
50,000 requests an hour                  Every request to ``/open_auth/``, per application
100 rejected credentials an hour         Requests that fail with ``invalid_client``,
                                         counted per application and address
======================================= ==================================================

When a limit is reached, Omniport answers ``429 Too Many Requests`` with a
``Retry-After`` header giving the number of seconds until the limit resets.

.. code-block::

  HTTP/1.1 429 Too Many Requests
  Retry-After: 1800

  {
    "detail": "Request was throttled. Expected available in 1800 seconds."
  }

.. warning::

  A ``429`` is not a failure of Omniport, and it is not an invalid request.
  Applications that present it to users as a generic error leave them with no
  way to know that signing in again shortly would work. Surface the wait, and
  retry no sooner than ``Retry-After`` says. Retrying immediately will be
  refused again and brings the limit no closer to resetting.

.. note::

  If you expect an event that will bring a large number of users to your
  application at once, tell IMG beforehand. Limits can be raised for a window,
  and load can be tested against a staging environment first.

Future plans
------------

The flow supports the ``authorization_code`` and ``refresh_token`` grant types.
This will eventually be expanded to support most if not all of the multitude of
flows backed by the OAuth2 specification.

Further reading
---------------

You should read the `official OAuth docs
<https://www.oauth.com/oauth2-servers/server-side-apps/example-flow/>`_ for more
theoretical information on OAuth2 and its many loosely-regulated forms.

For additional information on the parameters refer to the `documentation
<https://django-oauth-toolkit.readthedocs.io/en/latest/>`_ of the Django OAuth
Toolkit PyPI package.
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

========================= =====================================================================
Parameter                  Description
========================= =====================================================================
**client_id** (required)   The client ID you obtained from the dashboard
**redirect_uri**           One of the redirect URIs you have registered on the dashboard
**state**                  Any string that you want the ``REDIRECT_URI`` to receive on success
========================= =====================================================================

.. warning::

  If the ``redirect_uri`` does not match any of the listed redirect URIs, the 
  authorisation request will fail and the user will not see an authorisation 
  screen.

.. note::

  For additional information on the query parameters refer to the
  `documentation <https://django-oauth-toolkit.readthedocs.io/en/latest/>`_ of
  the Django OAuth Toolkit PyPI package.

A sample authorisation request URL could therefore look like the one below.

::
  
  /oauth/authorise/?client_id=MY_CLIENT_ID
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
          ],
          ...
       },
       "student": {
            "enrolmentNumber": "15xxx009",
             ...
       },
       "contactInformation": {
            "instituteWebmailAddress": "xyz@iitr.ac.in"
             ...
       }
    }

However, if the access token is invalid, you will receive the following ``401 Unauthorized`` error response.

.. code-block::

    {
        "detail": "Authentication credentials were not provided."
    }

Generating new access token using refresh token
------------------------------------

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
------------------------------------

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

Future plans
------------

As of now the OAuth2 flow supports only the ``authorisation_code`` grant type
in the flow. This will eventually be expanded to support most if not all of the
multitude of flows backed by the OAuth2 specification.

Further reading
---------------

You should read the `official OAuth docs
<https://www.oauth.com/oauth2-servers/server-side-apps/example-flow/>`_ for more
theoretical information on OAuth2 and its many loosely-regulated forms.

For additional information on the parameters refer to the `documentation
<https://django-oauth-toolkit.readthedocs.io/en/latest/>`_ of the Django OAuth
Toolkit PyPI package.
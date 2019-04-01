App header
==========

The *app header* is always attached to the top of the app and shows information 
about the app or site such as its logo, name and user information.

Props
-----

#. ``mode``
    
    :Type:
      ``enum (string)``
    :Default:
      ``site``
    :Description:
      | defines if ``AppHeader`` should display app-related branding or 
        site-related branding
      | **Enums:**  ``site``, ``app``

#. ``appName``
    
    :Type:
      ``string``
    :Conditions for use:
      prop ``mode`` has value ``app``
    :Default:
      **\*required**
    :Description:
      | used to get corresponding assets and app ``baseUrl`` from backend as 
        well as frontend configs
      | Note: **NOT** ``appVerboseName``

#. ``sidebarButton``
  
    :Type:
      ``Boolean``
    :Default:
      ``false``
    :Description:
      | whether to display sidebar button to the left of the logo

#. ``sideBarVisibility``

    :Type:
      ``Boolean``
    :Conditions for use:
      prop ``sideBarButton`` has value ``true``
    :Default:
      ``false``
    :Description:
      | whether the sidebar is opened (visible, ``true``) or closed (hidden,
        ``false``)

#. ``onSidebarClick``

    :Type:
      ``function()``
    :Conditions for use:
      prop ``sideBarButton`` has value ``true``
    :Default:
      ``null``
    :Description:
      | the function that will be called when sidebar button is clicked

#. ``hamburgerOptions``

    :Type:
      ``[string]``
    :Conditions for use:
      prop ``sideBarButton`` has value ``true``
    :Default:
      .. code-block:: javascript

        [
          'hamburger--minus',
          'hamburger--spin', 
          'hamburger--squeeze'
        ]

    :Description:
        | types of hamburger animations
        | Accepts any subset of the default list
        | For more information, `click here <https://jonsuh.com/hamburgers/>`_

#. ``userDropdown``

    :Type:
      ``Boolean``
    :Default:
      ``false``
    :Description:
      | whether to display sign in button or user details and notification bell
      | Displays institute logo, wordmark or name depending on availability

#. ``middle``

    :Type:
      ``<ReactNode>``
    :Default:
      ``null``
    :Description:
      | element, if any, to be rendered in the middle of the header

#. ``right``

    :Type:
      ``<ReactNode>``
    :Default:
      ``null``
    :Description:
      | element, if any, to be rendered on the right side of the header

Example usage
-------------

.. code-block:: javascript

  import { AppHeader } from 'formula_one'

Importing ``AppHeader`` from ``formula_one``

.. code-block:: javascript
    
  const hamburgerOptions = [
    'hamburger--minus',
    'hamburger--spin'
  ]

Defining an array of strings to pass in ``hamburgerOptions``

.. code-block:: jsx

  <AppHeader
    mode='app'
    appName='placement_and_internship'
    sideBarButton={true}
    sideBarVisibility={this.state.sideBarVisibility}
    onSidebarClick={this.handleSidebarClick}
    hamburgerOptions={hamburgerOptions}
    userDropdown
  />

Using ``AppHeader`` in ``app`` mode 

It will render page title, favicon, app name and app logo by querying the
backend and handling all possible cases to render the best possible assets with
a user dropdown or 'Login' button based on whether a user is logged in.

.. code-block:: jsx

  <AppHeader
    mode='site'
    userDropdown
  />

Using ``AppHeader`` in ``site`` mode

It will render site page title, site favicon, site name and site logo by
querying the backend and handling all possible cases to render the best possible
assets with a user dropdown or 'Login' button based on whether a user is logged
in. .. code-block:: jsx

  <AppHeader />

Using ``AppHeader`` with absolutely no props

It will render the header in ``site`` mode and the institute logo in place of
the user dropdown.

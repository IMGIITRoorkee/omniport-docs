User card
=========

A user card is a component which displays the user's information in an 
organised way, in an aesthetic card. 

Props
-----

#. ``image``

    :Type:
      ``string``
    :Default:
      ``null``
    :Description:
      | the source to pass in the image tag's ``src`` attribute

#. ``name``

    :Type:
      ``string``
    :Default:
      **\*required**
    :Description:
      | the name of a user, used as heading in the card as well as the prop for
        :doc:`the default DP component <default_dp>`

#. ``size``

    :Type:
      ``string``
    :Default:
      ``'1.5em'``
    :Description:
      | directly passed as a prop to :doc:`the default DP component
        <default_dp>`

#. ``username``

    :Type:
      ``string``
    :Default:
      ``''``
    :Description:
      | the sub-heading for the user card

#. ``roles``

    :Type:
      ``[string]``
    :Default:
      ``''``
    :Description:
      | an array of role names as strings, that are joined with ``', '``

#. ``right``

    :Type:
      ``<ReactNode>``
    :Default:
      ``null``
    :Description:
      | the element to be shown on the right side of the component
      | This is generally used to pass icons like 'cross', 'close' or 'check'. 

Example usage
-------------

.. code-block:: javascript

  import { UserCard } from 'formula_one'

Importing ``UserCard`` from ``formula_one``

.. code-block:: javascript

  const roles = ['Student', 'Frontend developer']

Defining an array of strings to pass in ``roles``

.. code-block:: jsx
    
  <UserCard
      name='Praduman Goyal'
      username='pradumangoyal'
      roles={roles}
      image='/path/to/profile.jpg'
      size='3em'
      right={<Icon name='check' />}
  />

Using ``UserCard``, passing all the props

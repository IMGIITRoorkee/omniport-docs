Masonry layout
==============

Masonry layouts are those that display staggered grids where cells may be of
variable heights. This component is a wrapper around the similar components so
that all the children are positioned in a way that the columns have the minimum
difference between their bottom ends.

Props
-----

#. ``children``

    :Type:
      ::
      
        [
          <ReactNode 
            ... 
            image={Boolean} 
          />
        ]
    :Default:
      **\*required**
    :Usage:
      This prop differs from standard usage. See below.
    :Description:
      | the list of elements that is to be shown in a masonry layout


#. ``columns``

    :Type:
      ``number``
    :Default:
      ``2``
    :Description:
      | number of columns into which the list of elements is to be divided

#. ``gap``

    :Type:
      ``number``
    :Default:
      ``10``
    :Description:
      | gutter in between the columns of the layout

Example usage
-------------

.. code-block:: javascript

  import { MasonryLayout } from 'formula_one'

Importing ``MasonryLayout`` from ``formula_one``

.. code-block:: jsx

  <MasonryLayout columns={isBrowser ? 2 : 1} gap={28}>
    {feedList.map(feed => {
      return (
        <FeedCard
          key={feed.id}
          feed={feed}
          image={Boolean(feed.image)}
        />
      )
    })}
  </MasonryLayout>

Using ``MasonryLayout``, by passing number of columns and gap between them

.. note::

  ``children`` is a special prop that must be passed as actual children in the
  React shadow DOM. Notice here that ``children`` actually refers to the ``map``
  on ``feedList`` returning a list of ``FeedCard`` nodes.

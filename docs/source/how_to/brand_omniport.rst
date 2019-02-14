... brand Omniport?
===================

Omniport is the working title of the project. Your portal need not be named 
Omniport, although no one's going to stop you from naming it that if you prefer.

However, for those of us that would like to brand their specific instance of 
Omniport, branding has been made really really easy. Effortless actually.
Omniport supports deep branding of the portal to customise it thoroughly for 
your institute.

Destination
-----------

All paths referenced here lie within the ``omniport-backend/`` folder inside
the ``codebase/`` folder.

Instructions
------------

- **Follow the naming convention specified.** 

  Omniport is not sentient and will 
  not locate your images if not named and placed according to the pattern. To
  omit an asset, leave out the file.

- **Follow the size and aspect ratio guidelines.** 

  This is so that the assets 
  integrate harmoniously with the rest of the portal. As feature packed as 
  Omniport is, it is not free of assumptions.

- **Follow the file format specification.** 

  As a rule of thumb prefer `.svg`
  and `.ico` when the image needs to scale up and down respectively. Preferred 
  file formats are given, in order of preference, best stick to them.

- **All branding is optional.** 

  While a bit of imagery adds to the aesthetics,
  it is not essential. In its absence, everything will gracefully fallback on 
  textual branding defined in `configuration/`.

Image specifications
--------------------

================= ================== ================= ==============================
File name          Aspect ratio       Height in use     Formats
================= ================== ================= ==============================
``favicon.ico``    square             16, 32, 48 px     multisize ``.ico`` only
``logo.xyz``       square preferred   3.5em *(~49px)*   ``.svg``, ``.png``, ``.jpg``
``wordmark.xyz``   no restrictions    3.5em *(~49px)*   ``.svg``, ``.png``, ``.jpg``
================= ================== ================= ==============================

All images should be provided in 2x size if not supplying in the ``.svg`` format
to ensure that they work well on HiDPI displays.

For best results, use `RealFaviconGenerator <https://realfavicongenerator.net/>`_ to generate
your ``favicon.ico`` files.

Branding types
--------------

Batteries-included
++++++++++++++++++

The following files are required to brand Omniport with your custom branding. 
Defaults will be provided for these images.

- ``site/``: 

  Since Omniport allows you to run multiple sites (such as Intranet 
  and Internet) from the same portal, we allow you to brand them separately by 
  loading indexed files.

  Indexing works by suffixing ``_<side_id>`` to the folder name. So a logo for a 
  site with site ID 2 should be placed in ``site_2/`` for Omniport to recognise it. 
  This is optional and you can skip the indexing portion to use the same asset 
  across your sites. 
  
  Ensure that you brand all your served sites or provide a non-indexed version as 
  fallback. You may use the provided default Omniport branding for your portal or 
  *for reference* when designing your own, if designing your own.

  If not redesigning your own icons, be sure to respect the 
  :doc:`Brand usage guide <../legal/brand_usage_guide>`.

Batteries-not-included
++++++++++++++++++++++

The following files are required to brand Omniport with your custom branding. 
No defaults will be provided for these images.

- ``institute/``:

  Your institutes logo and wordmark should be used here. There are no defaults and
  no references for this set of imagery.

- ``maintainers/``:

  The branding imagery employed by Information Management Group for the Indian 
  Institute of Technology, Roorkee is available *for reference*.

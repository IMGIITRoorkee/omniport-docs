Django
======

This script builds the Django container that is responsible for operating the 
API powering Omniport.

.. code-block:: console

  [apps omniport-docker]$ ./scripts/build/django.sh

You will get the choice regarding the installation of developer tools. Affirm
with a :kbd:`Y` if you are going to be using the image for debugging, else
decline with any other character, primarily :kbd:`N`. If you are unsure, press
:kbd:`Y`, although this is not the default for image size concerns.

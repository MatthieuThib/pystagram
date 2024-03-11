===========
 Pystagram
===========

.. image:: https://raw.githubusercontent.com/MatthieuThib/pystagram/main/logo.svg
   :target: https://github.com/MatthieuThib/pystagram/
   :alt: Pystagram logo
   :align: right
   :width: 30%


`Home <https://github.com/MatthieuThib/pystagram>`_
• `Docs <https://readthedocs.org/projects/pystagram/>`_
• `PyPi <https://pypi.org/project/pystagram/>`_
• `Features`_
• `Installation`_
• `Usage`_
• `Contributors`_

|Python Version|  |GitHub Release| |PyPI| |PyPI Downloads| |Wheel|


**Pystagram** is a python client for Instagram APIs.

It provides a simple and easy to use interface for accessing endpoints of both `Graph <https://developers.facebook.com/docs/instagram-api>`_ and `Basic Display <https://developers.facebook.com/docs/instagram-basic-display-api>`_ APIs.


Features
=========

* Instagram Graph API:
    *  get and publish instagram media (posts, stories, reels)
    *  manage and reply to comments
    *  perform hashtag searches
    *  get metrics about Instagram Businesses and Creators.

* Instagram Basic Display API:
    *  get user profile information
    *  get user media


Installation
=============

PyPI (Python)
--------------

|PyPI|

.. code-block:: bash

   pip install pystagram

Source Code (Github)
---------------------

|GitHub Release|

.. code-block:: bash

    git clone https://github.com/MatthieuThib/pystagram.git
    cd pystagram
    pip install .


Usage
======

Setup account
--------------

In order to use the Instagram APIs (Graph API and Basic Display API), some prerequisites are required, follow the getting started guide to set up your account and get the necessary credentials:

* `Graph API <https://developers.facebook.com/docs/instagram-api/getting-started>`_
* `Basic Display API <https://developers.facebook.com/docs/instagram-basic-display-api/getting-started>`_

This will provide you with the following credentials:

* App ID
* App Secret
* Access Token

Instagram APIs use access tokens to authenticate requests. Those tokens are tied to specific permissions and can be generated for different purposes.
Before calling any endpoint, make sure that the access token has the necessary permissions to request the endpoint.

See the `Permissions <https://developers.facebook.com/docs/permissions>`_ page for more information.


Code examples
--------------

Instagram Graph API
^^^^^^^^^^^^^^^^^^^^

**Publishing a media**

.. code-block:: python

    import os

    # Importing the necessary modules
    from pystagram import PystagramGraphApi
    from pystagram.components.containers import ImageContainer

    # Initializing the PystagramGraphApi with the necessary credentials
    graph_api = PystagramGraphApi(
        app_id=int(os.getenv("APP_ID")),  # The App ID from the environment variables
        app_secret=os.getenv("APP_SECRET"),  # The App Secret from the environment variables
        access_token=os.getenv("ACCESS_TOKEN"),  # The Access Token from the environment variables
    )

    # Creating an ImageContainer with the image URL and caption
    container = ImageContainer(
        image_url="https://www.example.com/image.jpg",  # The URL of the image
        caption="your caption #hashtag",  # The caption for the image
        # Additional parameters can be added here
    )

    # Creating a media object with the ImageContainer
    response = graph_api.user.media.create(container)
    # Extracting the ID of the created media object
    container_id = response.data.get("id")

    # Publishing the created media object
    graph_api.user.media_publish.create(container_id=container_id)



Instagram Basic Display API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Fetch user media**

.. code-block:: python

    import os

    from pystagram import PystagramBasicDisplayApi
    from pystagram.components.fields import MediaFields

    # Instantiate the PystagramBasicDisplayApi class with the necessary credentials
    basic_display_api = PystagramBasicDisplayApi(
        app_id=int(os.getenv("APP_ID")),  # The App ID from the environment variables
        app_secret=os.getenv("APP_SECRET"),  # The App Secret from the environment variables
        access_token=os.getenv("ACCESS_TOKEN"),  # The Access Token from the environment variables
    )

    # Fetch the user's media from the API
    # The get() method sends a GET request to the API and returns the response
    response = basic_display_api.user.user_media.get()

    # Extract the user's media data from the response
    user_media = response.data.get("data")


Paginated endpoints
--------------------

Both APIs feature paginated endpoints, which means that the response of a request can be split into multiple pages. The pystagram library handles this by decorating the endpoints' methods with a custom decorator `@cursor_paginated`. When called, the decorated method will iterate over all the pages until there is no more pages to fetch or the maximum number of pages is reached.
By default, the maximum number of pages is set to **None** (ie. no limit), but it can be changed by passing setting the attribute **MAX_PAGES** of the class to a different integer value.

.. code-block:: python

    from pystagram import PystagramGraphApi

    # Initializing the PystagramGraphApi with the necessary credentials
    graph_api = PystagramGraphApi( ... )

    # Set the maximum number of pages to fetch from the API
    graph_api.MAX_PAGES = 5

    # Request a cursor paginated endpoint
    response = graph_api.user.media.get()


Contributors
=============

|Contributors|

.. |GitHub Release| image:: https://img.shields.io/github/v/release/MatthieuThib/pystagram
   :target: https://github.com/MatthieuThib/pystagram/releases/latest
   :alt: GitHub Release

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pystagram
   :target: https://pypi.org/project/pystagram
   :alt: Python Version

.. |PyPI| image:: https://img.shields.io/pypi/v/pystagram.svg?label=pip&logo=PyPI&logoColor=white
   :target: https://pypi.org/project/pystagram
   :alt: PyPI

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/pystagram.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold
   :target: https://pypi.org/project/pystagram
   :alt: PyPI Downloads

.. |Wheel| image:: https://img.shields.io/pypi/wheel/pystagram
   :target: https://pypi.org/project/pystagram
   :alt: PyPI

.. |Contributors| image:: https://contrib.rocks/image?repo=MatthieuThib/pystagram
   :target: https://github.com/MatthieuThib/pystagram/graphs/contributors
   :alt: Contributors
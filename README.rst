|Banner|

`Website <https://pystagram.org>`_
• `Docs <https://readthedocs.org/projects/pystagram/>`_
• `PyPi <https://pypi.org/project/pystagram/>`_
• `Features`_
• `Installation`_
• `Usage`_

|CI| |Python Version| |Coverage| |PyPI| |PyPI Downloads|

|

**Pystagram** is a python client for Instagram APIs.
It provides a simple and easy to use interface for accessing endpoints of both `Graph API <https://developers.facebook.com/docs/instagram-api>`_ and `Basic Display API <https://developers.facebook.com/docs/instagram-basic-display-api>`_.


Features
===========

* Instagram Graph API:
    *  get and publish instagram media (posts, stories, reels)
    *  manage and reply to comments
    *  perform hashtag searches
    *  get metrics about Instagram Businesses and Creators.

* Instagram Basic Display API:
    *  get user profile information
    *  get user media


Installation
===========

PyPI (Python)
-------------

|PyPI|

.. code-block:: bash

   pip install pystagram

Source Code (Github)
-------------------

|GitHubRealease|

.. code-block:: bash

    git clone https://github.com/MatthieuThib/pystagram.git
    cd pystagram
    pip install .


Usage
=====

Setup account
-------------

In order to use the Instagram APIs (Graph API and Basic Display API), you need to create an app on the `Facebook for Developers <https://developers.facebook.com/>`_ platform and obtain an access token.


client id client secret in environment variables

Access token
------------

Instagram APIs use access tokens to authenticate requests.



Code examples
------------

Graph API
^^^^^^^^^^^^

**Publishing a media**

.. code-block:: python

    import os

    # Importing the necessary modules
    from pystagram.components.containers import ImageContainer
    from pystagram.graph_api import PystagramGraphApi

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



Basic Display API
^^^^^^^^^^^^

**Fetch user media**

.. code-block:: python

    import os

    from pystagram.basic_display_api import PystagramBasicDisplayApi
    from pystagram.components.fields import MediaFields

    # Instantiate the PystagramBasicDisplayApi class with the necessary credentials
    basic_display_api = PystagramBasicDisplayApi(
        app_id=int(os.getenv("APP_ID")),  # The App ID from the environment variables
        app_secret=os.getenv("APP_SECRET"),  # The App Secret from the environment variables
        access_token=os.getenv("ACCESS_TOKEN"),  # The Access Token from the environment variables
    )

    # Set the maximum number of pages to fetch from the API
    basic_display_api.MAX_PAGES = 5

    # Fetch the user's media from the API
    # The get() method sends a GET request to the API and returns the response
    response = basic_display_api.user.user_media.get()

    # Extract the user's media data from the response
    user_media = response.data.get("data")


Paginated endpoints
-------------------

Both APIs feature paginated endpoints, which means that the response of a request can be split into multiple pages. The pystagram library handles this by decorating the endpoints' methods with a custom decorator `@cursor_paginated`. When called, the decorated method will iterate over all the pages until there is no more pages to fetch or the maximum number of pages is reached.
By default, the maximum number of pages is set to **None** (ie. no limit), but it can be changed by passing setting the attribute **MAX_PAGES** of the class to a different integer value.






.. |Banner| image:: https://pystagram.org/img/logo-github-readme.png
   :target: https://pystagram.org
   :alt: DVC logo

.. |VS Code Extension Overview| image:: https://raw.githubusercontent.com/iterative/vscode-pystagram/main/extension/docs/overview.gif
   :alt: DVC Extension for VS Code

.. |CI| image:: https://github.com/iterative/pystagram/workflows/Tests/badge.svg?branch=main
   :target: https://github.com/iterative/pystagram/actions
   :alt: GHA Tests

.. |Maintainability| image:: https://codeclimate.com/github/iterative/pystagram/badges/gpa.svg
   :target: https://codeclimate.com/github/iterative/pystagram
   :alt: Code Climate

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pystagram
   :target: https://pypi.org/project/pystagram
   :alt: Python Version

.. |Coverage| image:: https://codecov.io/gh/iterative/pystagram/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/iterative/pystagram
   :alt: Codecov

.. |Snap| image:: https://img.shields.io/badge/snap-install-82BEA0.svg?logo=snapcraft
   :target: https://snapcraft.io/pystagram
   :alt: Snapcraft

.. |Choco| image:: https://img.shields.io/chocolatey/v/pystagram?label=choco
   :target: https://chocolatey.org/packages/pystagram
   :alt: Chocolatey

.. |Brew| image:: https://img.shields.io/homebrew/v/pystagram?label=brew
   :target: https://formulae.brew.sh/formula/pystagram
   :alt: Homebrew

.. |Conda| image:: https://img.shields.io/conda/v/conda-forge/pystagram.svg?label=conda&logo=conda-forge
   :target: https://anaconda.org/conda-forge/pystagram
   :alt: Conda-forge

.. |PyPI| image:: https://img.shields.io/pypi/v/pystagram.svg?label=pip&logo=PyPI&logoColor=white
   :target: https://pypi.org/project/pystagram
   :alt: PyPI

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/pystagram.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold
   :target: https://pypi.org/project/pystagram
   :alt: PyPI Downloads

.. |Packages| image:: https://img.shields.io/badge/deb|pkg|rpm|exe-blue
   :target: https://pystagram.org/doc/install
   :alt: deb|pkg|rpm|exe

.. |DOI| image:: https://img.shields.io/badge/DOI-10.5281/zenodo.3677553-blue.svg
   :target: https://doi.org/10.5281/zenodo.3677553
   :alt: DOI

.. |Flowchart| image:: https://pystagram.org/img/flow.gif
   :target: https://pystagram.org/img/flow.gif
   :alt: how_pystagram_works

.. |Contribs| image:: https://contrib.rocks/image?repo=iterative/pystagram
   :target: https://github.com/iterative/pystagram/graphs/contributors
   :alt: Contributors

.. |VS Code| image:: https://img.shields.io/visual-studio-marketplace/v/Iterative.pystagram?color=blue&label=VSCode&logo=visualstudiocode&logoColor=blue
   :target: https://marketplace.visualstudio.com/items?itemName=Iterative.pystagram
   :alt: VS Code Extension
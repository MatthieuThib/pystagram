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

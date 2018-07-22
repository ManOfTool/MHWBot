import os
import cloudinary
import cloudinary.api


CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN', 'DEFAULT')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET', 'DEFAULT')
WIT_ACCESS_TOKEN = os.getenv('WIT_ACCESS_TOKEN', 'DEFAULT')

# cloudinary configuration
cloudinary.config(
	cloud_name = os.getenv('CLOUD_NAME', 'DEFAULT'),
	api_key = os.getenv('API_KEY', 'DEFAULT'),
	api_secret = os.getenv('API_SECRET', 'DEFAULT')
)

LUNASTRA = os.getenv('LUNASTRA', 'DEFAULT')
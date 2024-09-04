
from dotenv import dotenv_values

def api_url():
 config = dotenv_values(".env")
 return config['API_URL']

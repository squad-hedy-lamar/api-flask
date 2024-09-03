from flask import Flask

app = Flask(__name__, template_folder='templates')

import routes.episodes
import routes.characters
import routes.locations


# from utils.config import api_url

# API_URL = api_url()

# print(API_URL)
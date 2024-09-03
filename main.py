from flask import Flask

app = Flask(__name__, template_folder='templates')

import routes.episodes
import routes.characters
import routes.locations



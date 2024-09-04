from flask import Flask


app = Flask(__name__, template_folder='templates')

import routes.episodes
import routes.characters
import routes.locations

if __name__ == '__main__':
    app.run(debug=True)
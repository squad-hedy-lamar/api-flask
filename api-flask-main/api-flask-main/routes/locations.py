from main import app
from flask import render_template
from utils.config import api_url

API_URL = api_url()

# Desenvovler os métodos a partir daqui

@app.route("/locations")
def get_locations():
  # fazer aqui a chama da API
  return render_template('/locations/list.html', data={})


@app.route("/locations/<id>")
def get_location(id):
  # fazer aqui a chama da API
  return render_template('/locations/details.html', data={})
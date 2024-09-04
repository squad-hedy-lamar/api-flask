from main import app
from flask import render_template
from utils.config import api_url

API_URL = api_url()

# Desenvovler os métodos a partir daqui

@app.route("/characters")
def get_characters():
  # fazer aqui a chamada da API
  return render_template('/characters/list.html', active_tab='characters', data={})


@app.route("/characters/<id>")
def get_character(id):
  # fazer aqui a chamada da API
  return render_template('/characters/details.html', active_tab='characters', data={})
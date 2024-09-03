from main import app
from flask import render_template
from utils.config import api_url

API_URL = api_url()

@app.route("/episodes")
def get_episodes():
  # fazer aqui a chama da API
  return render_template('/episodes/list.html', data={})


@app.route("/episodes/<id>")
def get_episode(id):
  # fazer aqui a chama da API
  return render_template('/episodes/details.html', data={})

  
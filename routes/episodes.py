from main import app
from flask import render_template
from utils.config import api_url

API_URL = api_url()

@app.route("/episodes")
def get_episodes():
  return render_template('/episodes/list.html', data={})




  
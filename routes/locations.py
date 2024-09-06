from main import app
from flask import render_template
from utils.config import api_url
import urllib.request
import json

API_URL = api_url()

# Desenvolver os métodos a partir daqui
#"id":2,"name":"Abadango","type":"Cluster","dimension":"unknown"
@app.route("/locations")
def get_locations():
  # fazer aqui a chamada da API
  url = f"{API_URL}/location"
  response = urllib.request.urlopen(url)
  locations = response.read().decode("utf-8")
  data = json.loads(locations)


  
  return render_template('/locations/list.html', active_tab='locations', data={"locations": data['results']})


@app.route("/locations/<id>")
def get_location(id):
  # fazer aqui a chamada da API
  url = f"{API_URL}/location/{id}"
  response = urllib.request.urlopen(url)
  locations= response.read().decode("utf-8")
  data = json.loads(locations)
  
  
  return render_template('/locations/details.html', active_tab='locations',  data={"locations": data})


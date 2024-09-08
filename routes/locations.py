from main import app
from flask import render_template
from utils.config import api_url
import urllib.request
import json

API_URL = api_url()


# Desenvolver os métodos a partir daqui
# "id":2,"name":"Abadango","type":"Cluster","dimension":"unknown"
@app.route("/locations")
def get_locations():
    # Fazer a chamada da API
    url = f"{API_URL}/location"
    response = urllib.request.urlopen(url)
    json_data = response.read().decode("utf-8")  # JSON bruto
    data = json.loads(json_data)  # Converter JSON para dicionário Python

    # Passar dados para o template com a chave 'locations'
    return render_template(
        "/locations/list.html", active_tab="locations", locations=data["results"]
    )


@app.route("/locations/<id>")
def get_location(id):
    # Fazer a chamada da API
    url = f"{API_URL}/location/{id}"
    response = urllib.request.urlopen(url)
    json_data = response.read().decode("utf-8")  # JSON bruto
    location = json.loads(json_data)  # Converter JSON para dicionário Python

    # Passar dados para o template com a chave 'location'
    return render_template(
        "/locations/details.html", active_tab="locations", location=location
    )

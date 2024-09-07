from main import app
from flask import render_template
from utils.config import api_url
import urllib.request, json

API_URL = api_url()

# Desenvovler os métodos a partir daqui


@app.route("/character")
def get_characters():
    # fazer aqui a chamada da API
    url = f"{API_URL}/character"
    response = urllib.request.urlopen(url)
    characters = response.read().decode("utf-8")
    data = json.loads(characters)

    characters_list = []

    for character in data["results"]:
        character_info = {
            "id": character["id"],
            "name": character["name"],
            "species": character["species"],
            "gender": character["gender"],
            "origin": character["origin"],
            "location": character["location"],
        }
        characters_list.append(character_info)

        return render_template(
            "/characters/list.html",
            active_tab="characters",
            data={"chacters": characters_list},
        )

    characters_list = []

    for character in data['results']:
      character_info = {
        "id": character['id'],
        "name": character['name'],
        "species": character['species'],
        "gender": character['gender'],
        "origin": character['origin'],
        "location": character['location']
      }
      characters_list.append(character_info)
    return render_template('/characters/list.html', active_tab='characters', data={"chacters": characters_list})

@app.route("/character/<id>")
def get_character(id):
    # fazer aqui a chamada da API
    url = f"{API_URL}/characters/{id}"
    response = urllib.request.urlopen(url)
    character = response.read().decode("utf-8")
    data = json.loads(character)

    # lista de episódios
    episodes_list = [episode_url for episode_url in data["episode"]]

    return render_template(
        "/character/details.html",
        active_tab="characters",
        data={"character": data, "episodes": episodes_list},
    )

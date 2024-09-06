from main import app
from flask import render_template, request, jsonify
from utils.config import api_url
import urllib.request
import json

API_URL = api_url()


@app.route("/episodes")
def get_episodes():
    # fazer aqui a chama da API
    url = f"{API_URL}/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read().decode("utf-8")
    data = json.loads(episodes)

    episodes_list = []

    for episode in data["results"]:
        episode_info = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
        }
        episodes_list.append(episode_info)

    return render_template(
        "/episodes/list.html", active_tab="episodes", data={"episodes": episodes_list}
    )


@app.route("/episodes/<id>")
def get_episode(id):
    # fazer aqui a chama da API
    url = f"{API_URL}/episode/{id}"
    response = urllib.request.urlopen(url)
    episode = response.read().decode("utf-8")
    data = json.loads(episode)

    characters_list = getInfoCharacters(data["characters"])
    return render_template(
        "/episodes/details.html", active_tab="episodes", data={"episode": data, "characters": characters_list}
    )

def getInfoCharacters(characters):
  characters_list = []
  for character_url in characters:
    parts = character_url.split('/')
    id = parts[-1]

    character_info = {
      "id": id,
      "avatar": f"{API_URL}/character/avatar/{id}.jpeg",
      "url": character_url,
    }
    characters_list.append(character_info)

  return characters_list
    


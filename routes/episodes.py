from main import app
from flask import render_template

@app.route("/episodes")
def get_episodes():
  return render_template('/episodes/list.html', data={})




  
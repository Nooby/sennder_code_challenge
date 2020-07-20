from flask import render_template

from app import app
from app.ghibli import Ghibli


ghibli = Ghibli()


@app.route("/movies")
def index():
    films = ghibli.films()
    people = ghibli.people()
    for film in films:
        ID = film['id']
        if ID in people:
            film['people'] = people[ID]
        else:
            film['people'] = None
    return render_template('movies.html', films=films)

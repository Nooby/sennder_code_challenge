#!/usr/bin/env python3
from flask import Flask, render_template
from ghibli import Ghibli


app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

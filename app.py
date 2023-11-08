import flask
import csv
import json

app = flask.Flask(__name__)
new_list_of_movies = []
with open('imdb-movie-data.csv', 'r', encoding = 'utf-8') as file_with_list_of_movies:
    format_file = csv.reader(file_with_list_of_movies, delimiter = ',')
    for i in format_file:
        new_list_of_movies.append(i)

@app.route("/<genre>")
def main(genre):
    temp = [[i or None for i in raw] for raw in new_list_of_movies[1:] if genre.title() in raw[2]]
    return json.dumps([dict(zip(new_list_of_movies[0], i)) for i in temp], separators = (',', ':'))

@app.route("/")
def request():
    genre = flask.request.args.get("genre", default = None, type = str)
    temp = [[i or None for i in raw] for raw in new_list_of_movies[1:] if genre.title() in raw[2]]
    return json.dumps([dict(zip(new_list_of_movies[0], i)) for i in temp], separators = (',', ':'))

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080)
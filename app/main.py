from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv
from app import tmdb_client  # <-- KLUCZOWE

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    list_type = request.args.get("list_type", "popular")
    movies = tmdb_client.get_movies_list(list_type)  # <-- KLUCZOWE
    print("MOVIES:", movies)  # <-- debug: sprawdzamy co zwraca API!
    return render_template("home.html", movies=movies, list_type=list_type)

@app.route("/trending")
def trending():
    movies = tmdb_client.get_movies_list("now_playing")
    return render_template("trending.html", movies=movies)

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return render_template("search_results.html", movies=[], query=query)
    
    endpoint = f"search/movie?query={query}&language=pl-PL"
    data = tmdb_client.call_tmdb_api(endpoint)
    results = data.get("results", [])
    return render_template("search_results.html", movies=results, query=query)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
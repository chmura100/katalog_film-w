from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/trending")
def trending():
    api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    movies = data.get("results", [])
    return render_template("trending.html", movies=movies)

@app.route("/search")
def search():
    query = request.args.get("query")
    api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=pl-PL&query={query}"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])
    return render_template("search_results.html", movies=results, query=query)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pl-PL"
    response = requests.get(url)
    movie = response.json()
    return render_template("movie_details.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
    
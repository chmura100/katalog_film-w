import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
print(">>> API_TOKEN:", API_TOKEN)  # DEBUG: sprawdzamy czy token się wczytuje

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    print(">>> FULL URL:", full_url)     # DEBUG
    print(">>> HEADERS:", headers)       # DEBUG

    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

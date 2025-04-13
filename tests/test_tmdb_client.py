from unittest.mock import Mock
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import tmdb_client


def test_get_single_movie(monkeypatch):
    mock_data = {"title": "Mock Movie", "id": 123}
    mock_requests = Mock()
    mock_response = mock_requests.return_value
    mock_response.json.return_value = mock_data
    monkeypatch.setattr("app.tmdb_client.requests.get", mock_requests)
    result = tmdb_client.get_single_movie(movie_id=123)
    assert result == mock_data


def test_get_movie_images(monkeypatch):
    mock_images_data = {
        "backdrops": [{"file_path": "/image1.jpg"}],
        "posters": [{"file_path": "/poster1.jpg"}]
    }
    mock_requests = Mock()
    mock_response = mock_requests.return_value
    mock_response.json.return_value = mock_images_data
    monkeypatch.setattr("app.tmdb_client.requests.get", mock_requests)
    result = tmdb_client.get_movie_images(movie_id=456)
    assert result == mock_images_data


def test_get_single_movie_cast(monkeypatch):
    mock_cast_data = {
        "cast": [
            {"name": "Actor 1", "character": "Hero"},
            {"name": "Actor 2", "character": "Villain"}
        ]
    }
    mock_requests = Mock()
    mock_response = mock_requests.return_value
    mock_response.json.return_value = mock_cast_data
    monkeypatch.setattr("app.tmdb_client.requests.get", mock_requests)
    result = tmdb_client.get_single_movie_cast(movie_id=789)
    assert result == mock_cast_data
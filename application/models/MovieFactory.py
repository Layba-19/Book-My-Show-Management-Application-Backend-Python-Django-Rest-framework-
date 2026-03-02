from typing import Dict
from template.Movie import Movie


class MovieFactory:
    _movie_cache: Dict[str, Movie] = {}

    @classmethod
    def create_movie(cls, movie_id: int, name: str, duration: int) -> Movie:
        if name not in cls._movie_cache:
            cls._movie_cache[name] = Movie(movie_id, name, duration)
        return cls._movie_cache[name]

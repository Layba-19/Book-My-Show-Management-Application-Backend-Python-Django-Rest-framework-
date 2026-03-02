from typing import Dict, List, Optional

from application.enums.City import City
from application.template.Movie import Movie


class MovieController:
    def __init__(self):
        self.city_vs_movies: Dict[City, List[Movie]] = {}
        self.all_movies: List[Movie] = []

    # ADD movie to a particular city
    def add_movie(self, movie: Movie, city: City) -> None:
        self.all_movies.append(movie)

        movies = self.city_vs_movies.get(city, [])
        movies.append(movie)
        self.city_vs_movies[city] = movies

    # GET movie by name
    def get_movie_by_name(self, movie_name: str) -> Optional[Movie]:
        for movie in self.all_movies:
            if movie.get_movie_name() == movie_name:
                return movie
        return None

    # GET movies by city
    def get_movies_by_city(self, city: City) -> List[Movie]:
        return self.city_vs_movies.get(city, [])

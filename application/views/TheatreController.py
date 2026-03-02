from typing import Dict, List

from application.enums.City import City
from application.template.Movie import Movie
from application.template.Show import Show
from application.template.Theater import Theater


class TheatreController:
    def __init__(self):
        # City → [Theatre]
        self.city_vs_theatre: Dict[City, List[Theater]] = {}

        # [PVR, INOX, Cinepolis, Carnival]
        self.all_theatre: List[Theater] = []

    def add_theatre(self, theatre: Theater, city: City) -> None:
        self.all_theatre.append(theatre)

        theatres = self.city_vs_theatre.get(city, [])
        theatres.append(theatre)
        self.city_vs_theatre[city] = theatres

    def get_all_show(
        self,
        movie: Movie,
        city: City
    ) -> Dict[Theater, List[Show]]:
        """
        Returns:
        {
            Theatre1: [Show1, Show2],
            Theatre2: [Show3]
        }
        """

        theatre_vs_shows: Dict[Theater, List[Show]] = {}

        theatres = self.city_vs_theatre.get(city, [])
        # theatres = [PVR, INOX]

        for theatre in theatres:
            given_movie_shows: List[Show] = []

            shows = theatre.get_shows()
            # shows = [morning, evening]

            for show in shows:
                if show.get_movie().get_movie_id() == movie.get_movie_id():
                    given_movie_shows.append(show)

            if given_movie_shows:
                theatre_vs_shows[theatre] = given_movie_shows

        return theatre_vs_shows

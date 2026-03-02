from typing import List
from application.template.Movie import Movie
from application.template.Screen import Screen


class Show:
    def __init__(
        self,
        show_id: int = None,
        movie: Movie = None,
        screen: Screen = None,
        show_start_time: int = None,
        booked_seat_ids: List[int] = None
    ):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.show_start_time = show_start_time
        self.booked_seat_ids = (
            booked_seat_ids if booked_seat_ids is not None else []
        )

    # Getter and Setter for show_id
    def get_show_id(self):
        return self.show_id

    def set_show_id(self, show_id: int):
        self.show_id = show_id

    # Getter and Setter for movie
    def get_movie(self):
        return self.movie

    def set_movie(self, movie: Movie):
        self.movie = movie

    # Getter and Setter for screen
    def get_screen(self):
        return self.screen

    def set_screen(self, screen: Screen):
        self.screen = screen

    # Getter and Setter for show_start_time
    def get_show_start_time(self):
        return self.show_start_time

    def set_show_start_time(self, show_start_time: int):
        self.show_start_time = show_start_time

    # Getter and Setter for booked_seat_ids
    def get_booked_seat_ids(self):
        return self.booked_seat_ids

    def set_booked_seat_ids(self, booked_seat_ids: List[int]):
        self.booked_seat_ids = booked_seat_ids

from typing import List
from enums.City import City
from template.Movie import Movie
from models.MovieFactory import MovieFactory
from template.Screen import Screen
from template.Seat import Seat
from template.Show import Show
# from template.Theater import Theater
from models.TheaterFactory import TheatreFactory
from views.MovieController import MovieController
from views.TheatreController import TheatreController


class BookingDataFactory:

    @staticmethod
    def create_screens() -> List[Screen]:
        screens = []
        screen1 = Screen()
        screen1.set_screen_id(1)
        screen1.set_seats(BookingDataFactory.create_seats())
        screens.append(screen1)
        return screens

    @staticmethod
    def create_show(show_id: int, movie: Movie, show_start_time: int) -> Show:
        show = Show()
        show.set_show_id(show_id)
        show.set_movie(movie)
        show.set_show_start_time(show_start_time)
        return show

    @staticmethod
    def create_seats() -> List[Seat]:
        seats = []
        for i in range(1, 101):
            seat = Seat()
            seat.set_seat_id(i)
            seats.append(seat)
        return seats

    @staticmethod
    def create_movies(movie_controller: MovieController) -> List[Movie]:
        barbie = MovieFactory.create_movie(1, "BARBIE", 128)
        oppenheimer = MovieFactory.create_movie(2, "OPPENHEIMER", 180)

        movie_controller.add_movie(barbie, City.BANGALORE)
        movie_controller.add_movie(barbie, City.DELHI)
        movie_controller.add_movie(oppenheimer, City.BANGALORE)
        movie_controller.add_movie(oppenheimer, City.DELHI)

        return [barbie, oppenheimer]

    @staticmethod
    def create_theatres(
        movie_controller: MovieController,
        theatre_controller: TheatreController
    ) -> None:

        barbie = movie_controller.get_movie_by_name("BARBIE")
        oppenheimer = movie_controller.get_movie_by_name("OPPENHEIMER")

        inox = TheatreFactory.create_theatre(
            theatre_id=1,
            name="INOX",
            city=City.BANGALORE,
            shows=[
                BookingDataFactory.create_show(1, barbie, 10),
                BookingDataFactory.create_show(2, oppenheimer, 18)
            ]
        )

        pvr = TheatreFactory.create_theatre(
            theatre_id=2,
            name="PVR",
            city=City.DELHI,
            shows=[
                BookingDataFactory.create_show(3, barbie, 14),
                BookingDataFactory.create_show(4, oppenheimer, 20)
            ]
        )

        theatre_controller.add_theatre(inox, City.BANGALORE)
        theatre_controller.add_theatre(pvr, City.DELHI)

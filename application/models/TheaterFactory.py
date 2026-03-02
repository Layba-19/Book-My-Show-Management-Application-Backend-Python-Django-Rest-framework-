from typing import List
from enums.City import City
from template.Theater import Theater
from template.Screen import Screen
from template.Seat import Seat
from template.Show import Show


class TheatreFactory:

    @classmethod
    def create_theatre(
        cls,
        theatre_id: int,
        name: str,
        city: City,
        shows: List[Show]
    ) -> Theater:

        theatre = Theater()
        theatre.set_theatre_id(theatre_id)
        theatre.set_theatre_name(name)
        theatre.set_screens(cls._create_screens())
        theatre.set_city(city)
        theatre.set_shows(shows)

        return theatre

    @classmethod
    def _create_screens(cls) -> List[Screen]:
        screen = Screen()
        screen.set_screen_id(1)
        screen.set_seats(cls._create_seats())
        return [screen]

    @classmethod
    def _create_seats(cls) -> List[Seat]:
        seats = []
        for i in range(1, 101):
            seats.append(Seat(seat_id=i))
        return seats

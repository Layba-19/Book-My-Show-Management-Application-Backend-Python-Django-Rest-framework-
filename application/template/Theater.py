from typing import List
from application.enums.City import City
from application.template.Screen import Screen
from application.template.Show import Show


class Theater:
    def __init__(
        self,
        theatre_id: int = None,
        address: str = None,
        theatre_name: str = None,
        city: City = None,
        screens: List[Screen] = None,
        shows: List[Show] = None
    ):
        self.theatre_id = theatre_id
        self.address = address
        self.theatre_name = theatre_name
        self.city = city
        self.screens = screens if screens is not None else []
        self.shows = shows if shows is not None else []

    # Getter and Setter for theatre_id
    def get_theatre_id(self):
        return self.theatre_id

    def set_theatre_id(self, theatre_id: int):
        self.theatre_id = theatre_id

    # Getter and Setter for address
    def get_address(self):
        return self.address

    def set_address(self, address: str):
        self.address = address

    # Getter and Setter for theatre_name
    def get_theatre_name(self):
        return self.theatre_name

    def set_theatre_name(self, theatre_name: str):
        self.theatre_name = theatre_name

    # Getter and Setter for city
    def get_city(self):
        return self.city

    def set_city(self, city: City):
        self.city = city

    # Getter and Setter for screens
    def get_screens(self):
        return self.screens

    def set_screens(self, screens: List[Screen]):
        self.screens = screens

    # Getter and Setter for shows
    def get_shows(self):
        return self.shows

    def set_shows(self, shows: List[Show]):
        self.shows = shows

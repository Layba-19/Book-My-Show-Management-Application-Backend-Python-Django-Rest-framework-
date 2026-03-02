from typing import List
from application.template.Seat import Seat


class Screen:
    def __init__(self, screen_id: int = None, seats: List[Seat] = None):
        self.screen_id = screen_id
        self.seats = seats if seats is not None else []

    # Getter and Setter for screen_id
    def get_screen_id(self):
        return self.screen_id

    def set_screen_id(self, screen_id: int):
        self.screen_id = screen_id

    # Getter and Setter for seats
    def get_seats(self):
        return self.seats

    def set_seats(self, seats: List[Seat]):
        self.seats = seats

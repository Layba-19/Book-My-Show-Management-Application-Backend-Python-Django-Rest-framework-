from application.enums.SeatCategory import SeatCategory


class Seat:
    def __init__(
        self,
        seat_id: int = None,
        row: int = None,
        seat_category: SeatCategory = None
    ):

        # Getter and Setter for seat_id
        def get_seat_id(self):
            return self.seat_id

        def set_seat_id(self, seat_id: int):
            self.seat_id = seat_id

        # Getter and Setter for row
        def get_row(self):
            return self.row

        def set_row(self, row: int):
            self.row = row

        # Getter and Setter for seat_category
        def get_seat_category(self):
            return self.seat_category

        def set_seat_category(self, seat_category: SeatCategory):
            self.seat_category = seat_category

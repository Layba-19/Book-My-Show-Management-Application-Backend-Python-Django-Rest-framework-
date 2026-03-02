import uuid
from datetime import date
from typing import List, Dict

from enums.City import City
from views.MovieController import MovieController
from views.TheatreController import TheatreController
from template.Movie import Movie
from template.Show import Show
from template.Theater import Theatre
from models.BookingDataFactory import BookingDataFactory
from services.PaymentService import PaymentService


class BookingService:
    _instance = None  # Singleton instance

    def __init__(self):
        if BookingService._instance is not None:
            raise Exception("Use get_instance() to access BookingService")

        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = BookingService()
        return cls._instance

    # ---------------- MAIN FLOW ---------------- #

    def start_booking_session(self):
        self._print_header("🎬 Welcome to BookMyShow 🎟️")
        continue_booking = True

        while continue_booking:
            user_city = self._select_city()
            selected_movie = self._select_movie(user_city)
            selected_show = self._select_show(user_city, selected_movie)
            self._book_seat(selected_show)

            response = input(
                "Do you want to book another ticket? (yes/no): "
            ).strip().lower()
            continue_booking = response == "yes"

        self._print_success(
            "Thank you for using BookMyShow! 🎬 Have a great day!"
        )

    # ---------------- SELECTION METHODS ---------------- #

    def _select_city(self) -> City:
        self._print_section("🏙️ Select Your City")
        cities = list(City)

        for idx, city in enumerate(cities, start=1):
            print(f"   {idx}. {city.name}")

        return cities[self._get_user_choice(1, len(cities)) - 1]

    def _select_movie(self, city: City) -> Movie:
        movies = self.movie_controller.get_movies_by_city(city)
        self._print_section(f"🎥 Available Movies in {city.name}")

        for idx, movie in enumerate(movies, start=1):
            print(f"   {idx}. {movie.get_movie_name()}")

        return movies[self._get_user_choice(1, len(movies)) - 1]

    def _select_show(self, city: City, movie: Movie) -> Show:
        shows_map: Dict[Theatre, List[Show]] = (
            self.theatre_controller.get_all_show(movie, city)
        )

        available_shows: List[Show] = []
        self._print_section(
            f"🎭 Available Shows for {movie.get_movie_name()} in {city.name}"
        )

        index = 1
        for theatre, shows in shows_map.items():
            for show in shows:
                print(
                    f"   {index}. {show.get_show_start_time()}:00 "
                    f"at 🎦 {theatre.get_theatre_name()}"
                )
                available_shows.append(show)
                index += 1

        return available_shows[
            self._get_user_choice(1, len(available_shows)) - 1
        ]

    # ---------------- BOOKING ---------------- #

    def _book_seat(self, show: Show):
        self._print_section("💺 Select Your Seat (1-100)")
        seat_number = self._get_user_choice(1, 100)

        if seat_number in show.get_booked_seat_ids():
            print("❌ Seat already booked! Try another seat.")
            self._book_seat(show)
            return

        show.get_booked_seat_ids().append(seat_number)
        payment_service = PaymentService()
        payment_success = payment_service.process_payment(250)

        if payment_success:
            self._print_success("✅ Booking Successful! Enjoy your movie! 🍿")
            self._generate_ticket(show, seat_number)
        else:
            print("❌ Payment failed! Please try again.")
            show.get_booked_seat_ids().remove(seat_number)

    # ---------------- TICKET ---------------- #

    def _generate_ticket(self, show: Show, seat_number: int):
        print("\n========================================")
        print("🎟️       MOVIE TICKET CONFIRMATION       🎟️")
        print("========================================")
        print(f"🎬 Movie: {show.get_movie().get_movie_name()}")
        print(f"⏰ Show Time: {show.get_show_start_time()}:00")
        print(f"💺 Seat Number: {seat_number}")
        print("----------------------------------------")
        print(f"📅 Date: {date.today()}")
        print(f"🆔 Booking ID: {uuid.uuid4()}")
        print("========================================")
        print("🎉 Enjoy your movie! 🍿 Have a great time!")
        print("========================================\n")

    # ---------------- HELPERS ---------------- #

    def _get_user_choice(self, min_value: int, max_value: int) -> int:
        while True:
            try:
                choice = int(
                    input(f"👉 Enter choice ({min_value}-{max_value}): ")
                )
                if min_value <= choice <= max_value:
                    return choice
                print("❌ Choice out of range.")
            except ValueError:
                print("❌ Invalid input! Enter a number.")

    def _print_header(self, text: str):
        print("\n══════════════════════════════════════════")
        print(f"          {text}")
        print("══════════════════════════════════════════\n")

    def _print_section(self, text: str):
        print(f"\n🔹 {text}")
        print("──────────────────────────────────────────")

    def _print_success(self, text: str):
        print(f"\n🎉 {text}\n")

    # ---------------- INITIAL DATA ---------------- #

    def initialize(self):
        BookingDataFactory.create_movies(self.movie_controller)
        BookingDataFactory.create_theatres(
            self.movie_controller,
            self.theatre_controller
        )

class Movie:
    def __init__(
        self,
        movie_id: int = None,
        movie_name: str = None,
        movie_duration_in_minutes: int = None
    ):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_duration_in_minutes = movie_duration_in_minutes

    # Getter and Setter for movie_id
    def get_movie_id(self):
        return self.movie_id

    def set_movie_id(self, movie_id: int):
        self.movie_id = movie_id

    # Getter and Setter for movie_name
    def get_movie_name(self):
        return self.movie_name

    def set_movie_name(self, movie_name: str):
        self.movie_name = movie_name

    # Getter and Setter for movie_duration
    def get_movie_duration(self):
        return self.movie_duration_in_minutes

    def set_movie_duration(self, movie_duration: int):
        self.movie_duration_in_minutes = movie_duration

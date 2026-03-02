from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.views.MovieController import MovieController
from application.enums.City import City
from application.template.Movie import Movie

movie_controller = MovieController()


class AddMovieAPI(APIView):
    def post(self, request):
        name = request.data.get("name")
        city_param = request.data.get("city")

        if not name or not city_param:
            return Response(
                {"error": "name and city are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            city = City[city_param.upper()]
        except KeyError:
            return Response({"error": "Invalid city"}, status=400)

        movie = Movie(name)
        movie_controller.add_movie(movie, city)

        return Response(
            {"message": "Movie saved successfully"},
            status=status.HTTP_201_CREATED
        )


class GetMovieByNameAPI(APIView):
    def get(self, request):
        name = request.query_params.get("name")

        if not name:
            return Response(
                {"error": "name parameter is required"},
                status=400
            )

        movie = movie_controller.get_movie_by_name(name)

        if not movie:
            return Response(
                {"message": "Movie not found"},
                status=404
            )

        return Response({
            "movie_name": movie.get_movie_name()
        })


class GetMoviesByCityAPI(APIView):
    def get(self, request):
        city_param = request.query_params.get("city")

        if not city_param:
            return Response(
                {"error": "city parameter is required"},
                status=400
            )

        try:
            city = City[city_param.upper()]
        except KeyError:
            return Response({"error": "Invalid city"}, status=400)

        movies = movie_controller.get_movies_by_city(city)

        return Response([
            {"movie_name": m.get_movie_name()}
            for m in movies
        ])

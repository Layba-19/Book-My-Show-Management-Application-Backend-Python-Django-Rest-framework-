from django.urls import path

from application.views.movie_api import (
    AddMovieAPI,
    GetMovieByNameAPI,
    GetMoviesByCityAPI
)
from application.views.theatre_api import AddTheatreAPI

urlpatterns = [
    path('movie/', AddMovieAPI.as_view()),
    path('movie/by-name/', GetMovieByNameAPI.as_view()),
    path('movie/by-city/', GetMoviesByCityAPI.as_view()),
    path('theatre/', AddTheatreAPI.as_view()),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.views.TheatreController import TheatreController
from application.enums.City import City
from application.template.Theater import Theater

theatre_controller = TheatreController()


class AddTheatreAPI(APIView):
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

        theatre = Theater(name)
        theatre_controller.add_theatre(theatre, city)

        return Response(
            {"message": "Theatre saved successfully"},
            status=status.HTTP_201_CREATED
        )

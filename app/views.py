from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalSerializer


@api_view(["GET"])
def animals(reqeust):
    qs = Animal.objects.all()
    serializer = AnimalSerializer(instance=qs, many=True)
    return Response({"data": serializer.data})

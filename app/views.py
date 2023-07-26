from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Animal
from .serializers import AnimalSerializer
from .throttling import CSVRateThrottle

from django import db

import pandas as pd


class AnimalViews(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class CSVAPIView(APIView):
    throttle_classes = [CSVRateThrottle]

    def post(self, request):
        file = request.FILES["file"]
        objs = []

        try:
            df = pd.read_csv(file)
            for _, row in df.iterrows():
                x = Animal(
                    unique_id=row["unique_id"],
                    name=row["name"],
                    scientific_name=row["scientific_name"],
                    owner_name=row["owner_name"],
                    gender=row["gender"],
                    dob=row["dob"],
                    contact=row["contact"],
                    address=row["address"],
                )
                objs.append(x)
        except pd.errors.ParserError as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Animal.objects.bulk_create(objs=objs)
            return Response(
                {"detail": "Sucessfully inserted all rows"}, status=status.HTTP_200_OK
            )
        except db.IntegrityError:
            return Response(
                {"error": "Integrity error - file has already used 'unique_id' field"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except db.DatabaseError:
            return Response(
                {"error": "Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

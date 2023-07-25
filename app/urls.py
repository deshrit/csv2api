from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AnimalViews, CSVAPIView


router = DefaultRouter()
router.register("animals", AnimalViews)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/csv/", CSVAPIView.as_view(), name="csv"),
]

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("api/", include("app.urls")),
    # documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

from django.urls import path
from .views import SignupView

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('api/signup/', SignupView.as_view(), name="signup"),
    # path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
]

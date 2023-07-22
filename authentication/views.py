from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer


class SignupView(CreateAPIView):
    permission_classes = []
    serializer_class = SignupSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignupSerializer



class SignupView(CreateAPIView):
    permission_classes = []
    serializer_class = SignupSerializer


class BlacklistRefreshTokenView(APIView):

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)
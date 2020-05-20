import datetime
import jwt

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth import admin as auth_admin, get_user_model
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import update_last_login
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from accounts.api.serializers import UserSerializer, UpdatePasswordSerializer

User = get_user_model()

class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = []

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

class UserUpdatePasswordAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = UpdatePasswordSerializer(data=request.data)

        if serializer.is_valid():

            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # Set new password
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'password has been changed'
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            token = serializer.validated_data['access']
            decoded = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=decoded['user_id'])
            update_last_login(None, user)

        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            token = serializer.validated_data['access']
            decoded = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=decoded['user_id'])
            update_last_login(None, user)

        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
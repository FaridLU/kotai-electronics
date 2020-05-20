import datetime

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth import admin as auth_admin, get_user_model

from accounts.api.serializers import UserSerializer

User = get_user_model()

class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = []

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

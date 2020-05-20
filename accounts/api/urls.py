from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accounts.api.views import UserCreateAPIView, UserListAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('user-list/', UserListAPIView.as_view(), name='user-list'),
]
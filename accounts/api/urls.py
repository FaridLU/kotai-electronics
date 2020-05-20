from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accounts.api.views import UserCreateAPIView, UserListAPIView, CustomTokenObtainPairView, CustomTokenRefreshView, UserUpdatePasswordAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('user-list/', UserListAPIView.as_view(), name='user-list'),
    path('update-password/', UserUpdatePasswordAPIView.as_view(), name='update-password'),
    path('token/create/', CustomTokenObtainPairView.as_view(), name='token_create'),  # POST request (email, password is required)
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'), 
]
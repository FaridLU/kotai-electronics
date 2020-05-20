import datetime

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth import admin as auth_admin, get_user_model

from .serializers import TaskSerializer
from apptask.models import Task

User = get_user_model()

class TaskListApiView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = []
    queryset = Task.objects.all()

class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = []

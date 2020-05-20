from django.urls import path, include

from apptask.api.views import TaskListApiView, TaskCreateAPIView

urlpatterns = [
    path('task-list/', TaskListApiView.as_view(), name='task-list'), # new
    path('task-create/', TaskCreateAPIView.as_view(), name='task-create'), 
]

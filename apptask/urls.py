from django.urls import path, include
from apptask.views import CreateTaskView, ChangePassword, Home

app_name='apptask'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task-create/', CreateTaskView.as_view(), name='task-create'),
    path('password_change/', ChangePassword.as_view(), name='change-password'),
]

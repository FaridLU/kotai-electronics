from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView, TemplateView
from apptask.forms import TaskForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from apptask.models import Task

User = get_user_model()



# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'apptask/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'datas': Task.objects.all()
        })
        return context
    
class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'apptask/task-create.html'
    form_class = TaskForm
    success_url = '/'
    

class ChangePassword(LoginRequiredMixin, TemplateView):
    template_name = 'registration/change_passwords.html'

    def post(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        current_user.set_password(request.POST.get('new_password'))
        current_user.save()

        return HttpResponseRedirect('/')
from django import forms
from apptask.models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        exclude = ("created_date", "modified_date",)

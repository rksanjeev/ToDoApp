from django import forms
from django.forms import ModelForm
from todo.models import  Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields =  ('title', 'completed')

from testapp.models import Task
from django.forms import ModelForm

from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
from .models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['tasklist']
        #fields = '__all__'
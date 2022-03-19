from pyexpat import model
from attr import fields
from django.shortcuts import render, redirect
from .models import TaskList, Task
from .forms import TaskForm
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, FormView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'todolist/home.html'

class TaskListCreateView(CreateView):
    model = TaskList
    fields = '__all__'
    success_url = reverse_lazy('todolist:lists')

class TaskListListView(ListView):
    model = TaskList

class TaskListDetailView(DetailView):
    model = TaskList

    def tasks(self):
        return Task.objects.all()

class TaskListDeleteView(DeleteView):
    model = TaskList
    success_url = reverse_lazy('todolist:lists')

def addtask(request, pk):
    #pk = pk
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            Task.objects.create(name=f['name'], description=f['description'], deadline_date=f['deadline_date'], tasklist_id=pk)
            #form.save()
            return redirect(f'/list/{pk}')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_form.html', context={'form':form})

class TaskDetailView(DetailView):
    model = Task

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy(f'todolist:lists')
 

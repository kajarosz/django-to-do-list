from django.urls import path
from .views import HomeView, TaskListCreateView, TaskListListView, TaskListDetailView, TaskListDeleteView, TaskDetailView, TaskDeleteView
from . import views

app_name = 'todolist'

urlpatterns =  [
    path('', HomeView.as_view(), name='home'),
    path('addlist/', TaskListCreateView.as_view(), name='addlist'),
    path('lists/', TaskListListView.as_view(), name='lists'),
    path('list/<int:pk>/', TaskListDetailView.as_view(), name='tasklistdetails'),
    path('list/<int:pk>/addtask/', views.addtask, name='addtask'),
    #path('list/<int:pk>/addtask/', TaskCreateView.as_view(), name='addtask'),
    path('list/<int:pk>/delete/', TaskListDeleteView.as_view(), name="deletelist"),
    path('list/<int:list_id>/task/<int:pk>/', TaskDetailView.as_view(), name='taskdetails'),
    path('list/<int:list_id>/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='deletetask'),
]
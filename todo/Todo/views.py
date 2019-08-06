from django.views.generic import ListView, DetailView
from .models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "todo"





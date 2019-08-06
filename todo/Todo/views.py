from django.views.generic import ListView, DetailView, CreateView
from .models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = "todo"

class TodoCreateView(CreateView):
    template_name = 'Todo/todo_create.html'
    form_class = TodoCreateForm




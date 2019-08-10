from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Todo
from .forms import TodoCreateForm

"""
The django views for CRUD operations, the class names are very self-explanatory
"""


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = "todo"


class TodoCreateView(CreateView):
    template_name = 'Todo/todo_create.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('todo:todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description']
    template_name = "Todo/todo_update.html"
    success_url = reverse_lazy('todo:todo_list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:todo_list')
    template_name = "Todo/confirm_delete.html"
    success_message = 'Your Todo has been deleted successfully.'





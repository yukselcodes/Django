from django.urls import path

from .views import TodoListView, TodoDetailView, TodoCreateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('create/', TodoCreateView.as_view(), name='todo_create')

]
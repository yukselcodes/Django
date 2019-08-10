from django.urls import path

from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='todo_delete'),
]
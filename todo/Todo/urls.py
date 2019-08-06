from django.urls import path, include
from .views import TodoList, TodoDetail
urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('detail/<slug:title>', TodoDetail.as_view(), name='todo_detail'),


]
from django.urls import path, include
from . import views


urlpatterns = [
    path('departments', views.department_list),
    path('departments/<int:pk>', views.department_detail)
]

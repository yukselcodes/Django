from django.urls import path

from .views import department, course, student, professor


urlpatterns = [
    path('departments/', department.List.as_view(), name="department_list"),
    path('departments/detail/<int:pk>/', department.Detail.as_view(), name="department_detail"),
    path('departments/create/', department.Create.as_view(), name="department_create"),
    path('departments/update/<int:pk>/', department.Update.as_view(), name="department_update"),
    # path('courses/', course.List.as_view()),
    # path('courses/detail/<int:pk>/', course.Detail.as_view()),
    # path('courses/create/', course.Create.as_view()),
    # path('courses/update/<int:pk>/', course.Update.as_view()),
    path('students/', student.List.as_view(), name="student_list"),
    path('students/detail/<int:pk>/', student.Detail.as_view(), name="student_detail"),
    path('students/create/', student.Create.as_view()),
    path('students/update/<int:pk>/', student.Update.as_view()),
    # path('professors/', professor.List.as_view()),
    # path('professors/detail/<int:pk>/', professor.Detail.as_view()),
    # path('professors/create/', professor.Create.as_view()),
    # path('professors/update/<int:pk>/', professor.Update.as_view()),
]

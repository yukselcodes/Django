from rest_framework import generics

from ..models import Course
from ..serializers import CourseSerializer


class List(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Create(generics.CreateAPIView):
    serializer_class = CourseSerializer


class Update(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Detail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

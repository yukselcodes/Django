from rest_framework import generics

from ..models import Student
from ..serializers import StudentSerializer


class List(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Create(generics.CreateAPIView):
    serializer_class = StudentSerializer


class Update(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Detail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

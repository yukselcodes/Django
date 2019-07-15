from rest_framework import generics

from ..models import Department
from ..serializers import DepartmentSerializer


class List(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Create(generics.CreateAPIView):
    serializer_class = DepartmentSerializer


class Update(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Detail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

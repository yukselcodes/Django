from rest_framework import generics

from ..models import Professor
from ..serializers import ProfessorSerializer


class List(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class Create(generics.CreateAPIView):
    serializer_class = ProfessorSerializer


class Update(generics.RetrieveUpdateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class Detail(generics.RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

from .models import Student, Course, Professor, Department
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "surname", "gpa", "course", "department")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "capacity", "department")


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name", "code")


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ("id", "name", "surname", "interest_in", "department", "course")



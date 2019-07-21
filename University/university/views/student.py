from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..models import Department, Course, Professor, Student
from ..helper import Constants


class List(ListView):
    constants = Constants.get_constants("student", "list", "students", Student, 10)
    model = constants.get("MODEL_NAME", None)
    context_object_name = constants.get("CONTEXT_OBJECT_NAME", None)
    template_name = constants.get("TEMPLATE_NAME", None)
    object_list = []
    paginate_by = constants.get("PAGINATE_BY", 10)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print(context)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['students'] = self.get_queryset()
        return context

    def get_queryset(self):
        students = []
        all_students = Student.objects.all()
        for s in all_students:
            department = Department.objects.all().filter(id=s.department.id)
            students.append({'student': s, 'department': department})
        return students


class Detail(DetailView):
    constants = Constants.get_constants("student", "detail", "student", Student, 10)
    model = constants.get("MODEL_NAME", None)
    context_object_name = constants.get("CONTEXT_OBJECT_NAME", None)
    template_name = constants.get("TEMPLATE_NAME", None)
    object = {}
    paginate_by = constants.get("PAGINATE_BY", 10)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        s = Student.objects.get(pk=self.kwargs.get('pk'))
        department = Department.objects.all().filter(id=s.department.id)
        context['student'] = {'department': department, "student": s}
        return context


class Create(CreateView):
    constants = Constants.get_constants(template_file="student", action="create", model=Student)
    model = constants.get('MODEL_NAME', None)
    template_name = constants.get('TEMPLATE_NAME')
    fields = ("id", "name", "surname", "gpa", "course", "department")

    def get_success_url(self):
        return reverse_lazy('university:student_list')


class Update(UpdateView):
    constants = Constants.get_constants(template_file="student", action="update", model=Student)
    model = constants.get('MODEL_NAME', None)
    template_name = constants.get('TEMPLATE_NAME')
    fields = ("name", "surname", "gpa", "course", "department")

    def get_success_url(self):
        return reverse_lazy('university:student_detail', kwargs={'pk': self.kwargs['pk']})



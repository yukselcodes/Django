from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..models import Department, Course, Professor
from ..helper import Constants


class List(ListView):
    constants = Constants.get_constants("department", "list", "departments", Department, 10)
    model = constants.get("MODEL_NAME", None)
    context_object_name = constants.get("CONTEXT_OBJECT_NAME", None)
    template_name = constants.get("TEMPLATE_NAME", None)
    object_list = []
    paginate_by = constants.get("PAGINATE_BY", 10)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['departments'] = self.get_queryset()
        return context

    def get_queryset(self):
        departments = []
        all_departments = Department.objects.all()
        for d in all_departments:
            professors = Professor.objects.all().filter(department=d.id)
            courses = Course.objects.all().filter(department=d.id)
            departments.append({'department': d, 'courses': courses, "professors": professors})
        return departments


class Detail(DetailView):
    constants = Constants.get_constants("department", "detail", "department", Department, 10)
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
        d = Department.objects.get(pk=self.kwargs.get('pk'))
        courses = Course.objects.all().filter(department=d.id)
        professors = Professor.objects.all().filter(department=d.id)
        context['department'] = {'department': d, "courses": courses, "professors": professors}
        return context


class Create(CreateView):
    constants = Constants.get_constants(template_file="department", action="create", model=Department)
    model = constants.get('MODEL_NAME', None)
    template_name = constants.get('TEMPLATE_NAME')
    fields = ("id", "name", "code")

    def get_success_url(self):
        return reverse_lazy('university:department_list')


class Update(UpdateView):
    constants = Constants.get_constants(template_file="department", action="update", model=Department)
    model = constants.get('MODEL_NAME', None)
    template_name = constants.get('TEMPLATE_NAME')
    fields = ("name", "code")

    def get_success_url(self):
        return reverse_lazy('university:department_detail', kwargs={'pk': self.kwargs['pk']})





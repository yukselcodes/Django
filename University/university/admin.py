from django.contrib import admin
from . import models
# Register your models here.
_models = [models.Student, models.Professor, models.Course, models.Department]

admin.site.register(_models)

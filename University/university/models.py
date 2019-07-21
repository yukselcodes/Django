from django.db import models

"""
    This models represent the actors in the university
"""


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=5, null=False)

    def get_absolute_url(self):
        return reverse('department_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.code, self.name)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    capacity = models.IntegerField(null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.name, self.department)


class Professor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=False)
    interest_in = models.CharField(max_length=50)
    department = models.OneToOneField(Department, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('professor_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.name, self.surname)


class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    surname = models.CharField(null=False, max_length=20)
    gpa = models.FloatField(default=0.0)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.name, self.surname)






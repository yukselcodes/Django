from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'description')

    def __str__(self):
        return self.title

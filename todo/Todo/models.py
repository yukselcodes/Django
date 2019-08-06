from django.db import models
from django.urls import reverse

"""
This is the model for our Todo app 
"""


class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=60)

    class Meta:
        ordering = ('title',)
        unique_together = ('title', 'description')
        index_together = ('title', 'description')
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[self.title])

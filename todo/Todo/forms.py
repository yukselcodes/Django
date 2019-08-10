import django.forms as forms

from .models import Todo


class TodoCreateForm(forms.ModelForm):
    """
    A form handling form create action
    """
    class Meta:
        model = Todo
        fields = ('title', 'description')

    def filter_todo(self):
        """
        Checks if there is a todo same with to-be-created todo
        :return: title & description of todo
        """
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        if Todo.objects.filter(title=title, description=description).exists():
            raise forms.ValidationError('This to-do already exists!')
        return title, description

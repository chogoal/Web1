from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationFrom(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description']

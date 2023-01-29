
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_code', 'description',
                  'team', 'status', 'featured_image']
        required_fields = ['title', 'project_code', 'description',
                           'team', 'status', 'featured_image'],
        labels = {
            'title': "Project Title",
            'project_code': "Project Code",
            'description': "Details",
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            'title': {
                'min_length': "At least 3 chars",

                "required": "Please enter a title",
            },
            'project_code': {
                'min_length': "At least 6 chars",

                "required": "Please enter a 6 character code",
            },
            'description': {
                'min_length': "At least 9 chars",
                "required": "Please enter some more detrails",
            },

            'team': {
                "required": "Which team?",
            },
            'status': {
                "required": "Statusd",
            },
            'featured_image': {
                "required": "Image?",
            },
        }


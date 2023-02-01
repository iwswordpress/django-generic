from django.forms import ModelForm
from .models import Run


class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = ["run_name", "uploaded_filename"]
        required_fields = ["uploaded_filename"]
        labels = {"run_name": "Run Name", "uploaded_filename": "File"}
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            "run_name": {
                "required": "Please enter a RUN NAME",
            }
        }

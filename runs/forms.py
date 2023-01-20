from django.forms import ModelForm
from .models import Run


class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = ["run_name", "notebook_file"]
        required_fields = (["run_name", "notebook_file"],)
        labels = {
            "run_name": "Friendly Run Name",
            "notebook_file": "Notebook",
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            "run_name": {
                "min_length": "At least 3 chars",
                "required": "Please enter a run_name",
            },
            "notebooK_name": {
                "required": "Please add a file",
            },
        }


# class TestDataForm(ModelForm):
#     class Meta:
#         model = TestData
#         fields = "__all__"

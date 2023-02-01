from django.forms import ModelForm
from .models import Run


class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = ["run_name", "mlr_dataset"]
        required_fields = ["mlr_dataset"]
        labels = {"run_name": "Friendly Run Name", "mlr_dataset": "File"}
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            "mlr_dataset": {
                "min_length": "At least 3 chars",
                "required": "Please enter a mlr_dataset",
            }
        }

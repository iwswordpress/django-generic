from django.forms import ModelForm
from .models import UploadedFile


# class RunForm(ModelForm):
#     class Meta:
#         model = Run
#         fields = ["run_name", "uploaded_filename"]
#         required_fields = ["uploaded_filename"]
#         labels = {"run_name": "Run Name", "uploaded_filename": "File"}
#         # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
#         error_messages = {
#             "run_name": {
#                 "required": "Please enter a RUN NAME",
#             }
#         }


class UploadedFileForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["uploaded_name", "uploaded_filename"]
        required_fields = ["uploaded_filename"]
        labels = {
            "uploaded_name": "Uploaded Name",
            "uploaded_filename": "Uploaded File",
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            "uploaded_name": {
                "required": "Please enter a UPLOAD NAME",
            }
        }

from django import forms
from .validators import validate_email_domain


class CheckEmail(forms.Form):

    email = forms.EmailField(
        # required=False,
        validators=[validate_email_domain],
        widget=forms.EmailInput(attrs={"placeholder": "Your company email address"}),
    )

    def clean_email(self):
        return self.cleaned_data["email"].lower()


class AddFilm(forms.Form):

    name = forms.CharField(
        label="Film Name",
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Add your film"}),
    )

    def clean_name(self):
        output = f'<cleaned name to upper>: {self.cleaned_data["name"].upper()}'
        return output

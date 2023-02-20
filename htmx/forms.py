from django import forms
from django.core.exceptions import ValidationError
from .models import Team

# ++++++++++++++++++++++++++++++
# VALIDATORS


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address must be on the domain example.com.")


class RegisterForm:
    class Meta:
        model = Team
        fields = ["name"]


# ++++++++++++++++++++++++++++++
# FORM02


class OrderForm(forms.Form):

    email = forms.EmailField(
        required=False,
        # validators=[validate_email_domain],
        widget=forms.EmailInput(attrs={"placeholder": "Your company email address"}),
    )

    def clean_email(self):
        return self.cleaned_data["email"].lower()

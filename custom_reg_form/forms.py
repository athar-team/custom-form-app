from django import forms
from .models import UserFields
from django.utils.translation import gettext_lazy as _


class UserFieldsForm(forms.Form):
    age = forms.IntegerField(required=True)
    mobile_number = forms.CharField(required=True)
    job_title = forms.CharField(required=True)

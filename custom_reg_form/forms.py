from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields["age"].required = True
        self.fields["phone_number"].required = True
        self.fields["job_title"].required = True

    class Meta(object):
        model = ExtraInfo
        fields = (
            "age",
            "phone_number",
            "job_title"
        )
        labels = {
            "age": _("Age"),
            "phone_number": _("Phone number"),
            "job_title": _("Job Title"),
        }
        help_text = {
            "age": _("Please enter your Age"),
            "phone_number": _("Please enter your phone number"),
            "job_title": _("Please enter your job title"),
        }

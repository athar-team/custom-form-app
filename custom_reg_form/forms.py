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
        self.fields["nationality"].required = True
        self.fields["age"].required = True
        self.fields["gender"].required = True
        self.fields["phone_number"].required = True
        self.fields["qualification"].required = True
        self.fields["job_title"].required = True

    class Meta(object):
        model = ExtraInfo
        fields = (
            "nationality",
            "age",
            "gender",
            "phone_number",
            "qualification",
            "job_title"
        )
        labels = {
            "nationality": _("Nationality"),
            "age": _("Age"),
            "gender": _("Gender"),
            "phone_number": _("Phone number"),
            "qualification": _("Qualification"),
            "job_title": _("Job Title"),
        }
        help_text = {
            "nationality": _("Please enter your Nationality"),
            "age": _("Please enter your Age"),
            "gender": _("Please enter your gender"),
            "phone_number": _("Please enter your phone number"),
            "qualification": _("Please enter your qualification"),
            "job_title": _("Please enter your job title"),
        }

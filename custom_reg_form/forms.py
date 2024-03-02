from .models import UserFields
from django.forms import ModelForm


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields["age"].error_messages = {
            "required": "Please tell us your favorite movie.",
            "invalid": "We're pretty sure you made that movie up.",
        }
        self.fields["mobile_number"].error_messages = {
            "required": "Please tell us your favorite movie.",
            "invalid": "We're pretty sure you made that movie up.",
        }
        self.fields["job_title"].error_messages = {
            "required": "Please tell us your favorite movie.",
            "invalid": "We're pretty sure you made that movie up.",
        }

    class Meta(object):
        model = UserFields
        fields = ("age", "mobile_number", "job_title")

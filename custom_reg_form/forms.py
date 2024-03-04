from .models import UserFields
from django.forms import ModelForm


class UserFieldsForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(UserFieldsForm, self).__init__(*args, **kwargs)
        self.fields["mobile_number"].error_message = "Please tell us your favorite movie."
        self.fields["job_title"].error_message = "Please tell us your favorite movie."

    class Meta(object):
        model = UserFields
        fields = ("mobile_number", "job_title")

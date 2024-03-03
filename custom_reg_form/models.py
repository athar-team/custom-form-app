from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserFields(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    class Meta:
        db_table = "auth_userfields"
        permissions = (
            ("can_deactivate_users", "Can deactivate, but NOT delete users"),
        )

    user = models.OneToOneField(
        User, unique=True, db_index=True, related_name="info", on_delete=models.CASCADE
    )
    name = models.CharField(blank=True, max_length=255, db_index=True)

    mobile_number = models.CharField(verbose_name="Mobile Number", max_length=100)
    job_title = models.CharField(verbose_name="Job Title", max_length=100)

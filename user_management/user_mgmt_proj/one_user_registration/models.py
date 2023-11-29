from django.db import models
from django.contrib.auth.models import AbstractUser  # Abstractuser is used instead of User if we want to add custome fields
from django.core.exceptions import ValidationError


# Create your models here.

# we need to create a custom validation for validating mobile number
def mobile_number_validator(mobile_number):
    if not len(mobile_number) == 10:
        raise ValidationError(message="Mobile number should be 10 digits only ")
    if not mobile_number.isdigit():
        raise ValidationError(message="Mobile number should contain Numbers only ")


# creating Custom User model for custom fields
class CustomUser(AbstractUser):
    # by default it will have [username,password1,password2]
    # defining new custom field #mobile number
    mobile_number = models.CharField(max_length=10, blank=True, null=True, validators=[mobile_number_validator])

    def __str__(self):
        return self.username

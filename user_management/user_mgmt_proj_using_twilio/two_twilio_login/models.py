from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

#recreating User for practise

def mobile_number_validator(mobile_number):
    if not len(mobile_number) == 10:
        raise ValidationError(message="Mobile number should be 10 digits only")
    if not mobile_number.isdigit():
        raise ValidationError("Mobile number should only contain number only")

class CustomUser1(AbstractUser):
    mobile_number = models.CharField(max_length=10,blank=False,null=False,validators=[mobile_number_validator])

    def __str__(self):
        return self.username

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser1
from django.core.exceptions import ValidationError

def mobile_number_validator(mobile_number):
    if not len(mobile_number) == 10:
        raise ValidationError(message="Mobile number should be 10 digits only ")
    if not mobile_number.isdigit():
        raise ValidationError(message="Mobile number should contain Numbers only ")

def otp_validator(otp):
    if not len(otp) == 6:
        raise ValidationError(message="Mobile number should be 10 digits only ")
    if not otp.isdigit():
        raise ValidationError(message="Mobile number should contain Numbers only ")

#user registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=10,required=True,validators=[mobile_number_validator])

    # for overriding help_text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and set help_text to an empty string
        for field_name, field in self.fields.items():
            field.help_text = ''

    class Meta(UserCreationForm.Meta):
        model = CustomUser1
        fields = UserCreationForm.Meta.fields + ('mobile_number','email')


#forgot password
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


#otp login
class OTPLoginPassword(forms.Form):
    mobile_number = forms.CharField(max_length=10,required=True,validators=[mobile_number_validator])
    otp = forms.CharField(max_length=6,required=True,validators=[otp_validator])

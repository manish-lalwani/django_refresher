from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
def mobile_number_validator(mobile_number):
    if not len(mobile_number) == 10:
        raise ValidationError(message="Mobile number should be 10 digits only ")
    if not mobile_number.isdigit():
        raise ValidationError(message="Mobile number should contain Numbers only ")


class CustomUserCreationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10,required=False,validators=[mobile_number_validator])

    #for overriding help_text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and set help_text to an empty string
        for field_name, field in self.fields.items():
            field.help_text = ''

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('mobile_number',)
        # help_texts = {
        #     'username': None,
        #     'email': None,
        #     'password': None,
        #     'password1': None,
        #     'password2': None
        # }



from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                    'email',
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True

        if commit:
            user.save()

        return user

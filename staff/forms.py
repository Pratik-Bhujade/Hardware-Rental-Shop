from django import forms
from django.core.exceptions import ValidationError
from .models import *

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'

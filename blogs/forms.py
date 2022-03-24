import email
from django import forms
from .models import *
from django import forms

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['content']


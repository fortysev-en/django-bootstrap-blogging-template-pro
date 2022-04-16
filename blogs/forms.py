from django import forms
from .models import *

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['content']


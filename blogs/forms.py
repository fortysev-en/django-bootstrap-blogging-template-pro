from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['content']
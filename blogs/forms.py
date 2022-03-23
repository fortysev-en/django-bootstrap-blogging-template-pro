import email
from django import forms
from .models import *
from django import forms
from captcha.fields import ReCaptchaField

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['content']

class FormWithCaptcha(forms.Form):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    captcha = ReCaptchaField()


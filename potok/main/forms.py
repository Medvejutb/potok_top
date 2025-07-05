from django.forms import ModelForm
from django import forms
from .models import User


class Reg_from(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'tg',
            'password'
        ]


class Log_form(forms.Form):
    tg = forms.CharField(max_length=20)

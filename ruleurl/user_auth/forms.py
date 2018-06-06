from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        all_clean_data      = super().clean()
        password            = all_clean_data['password']
        confirm_password    = all_clean_data['password1']
        print(password)
        print(confirm_password)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Make sure password match")         
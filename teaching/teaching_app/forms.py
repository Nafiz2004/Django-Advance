from django import forms
from django.contrib.auth.models import User
from .models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class UserModelExtraForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['profile_pic']

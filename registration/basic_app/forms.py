from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .models import UserModel


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','password']


    password = forms.CharField(
                                widget=forms.PasswordInput(),
                                validators=[
                                            validators.MinLengthValidator(10)
                                            ]
    )

    email = forms.EmailField()
    
    def clean_email(self):

        email = self.cleaned_data['email']
        if not '@gmail' in email:
            raise forms.ValidationError('Only Gmail is supported')


class UserModelExtraForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['portfolio_site','profile_pic']

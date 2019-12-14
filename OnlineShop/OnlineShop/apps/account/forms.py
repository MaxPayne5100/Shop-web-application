from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import User

class SignInForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Wrong email or password")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Required. Please add a valid email address')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
from django import forms
# from django.contrib.auth.forms import UserCreationForm

class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=50)
    last_name = forms.CharField(label='Last Name',max_length=30)
    email = forms.EmailField()
    username = forms.CharField(label='Username',max_length=50)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=15, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=50)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()
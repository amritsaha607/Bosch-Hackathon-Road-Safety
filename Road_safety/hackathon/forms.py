from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)
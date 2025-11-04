from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.users.models import User

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

class LoginForm(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        model = User
        fields = (
            'username',
            'password'
        )
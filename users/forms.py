from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="email", max_length=254, help_text="Введите email для отправки")
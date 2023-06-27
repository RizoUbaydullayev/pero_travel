
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя *'})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль *'})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль *'})
    )
    email = forms.CharField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта *'})
    )
    first_name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
    )
    field_order = [
        'username',
        'email',
        'password1',
        'password2',
        'first_name',
        'last_name', 
    ]
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
        fields_classes = {'username': UsernameField}
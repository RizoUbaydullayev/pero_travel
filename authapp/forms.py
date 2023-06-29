
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': _('Имя пользователя *')})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': _('Пароль *')})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': _('Подтвердите пароль *')})
    )
    email = forms.CharField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': _('Электронная почта *')})
    )
    first_name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': _('Имя')})
    )
    last_name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': _('Фамилия')})
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


class CustomUserLoginForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(attrs={"autofocus": True, "placeholder": _('Имя пользователя')})
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': f"{_('Пароль')}"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }
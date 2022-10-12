import datetime

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core import validators

from .models import CustomUser


@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r"^\+{1}\d{11}"
    message = "Введите реальный номер телефона."
    flags = 0


class CustomUserRegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               label='Имя пользователя',
                               max_length=30,
                               validators=[UnicodeUsernameValidator()])
    email = forms.EmailField(required=True,
                             label='Email')
    phone = forms.CharField(required=True,
                            label='Номер телефона',
                            max_length=13,
                            initial='+375',
                            validators=[PhoneValidator()],
                            help_text="Введите номер в международном формате +375YYXXXXXXX")
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)
    birthday = forms.DateField(label='Дата рождения',
                               widget=forms.SelectDateWidget(years=range(datetime.date.today().year - 100,
                                                                         datetime.date.today().year)),
                               initial=datetime.date.today())
    interests = forms.CharField(label='Адрес',
                                max_length=500)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2', 'first_name', 'last_name', 'birthday',
                  'address']


# class CustomLoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
#     password = forms.CharField(
#         label="Пароль",
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
#     )

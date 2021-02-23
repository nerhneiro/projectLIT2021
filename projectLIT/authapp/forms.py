from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import SiteUser


class SiteUserLoginForm(AuthenticationForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(SiteUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_signin'


class SiteUserRegisterForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SiteUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_register'
            field.help_text = ''



class SiteUserEditForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'first_name', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super(SiteUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


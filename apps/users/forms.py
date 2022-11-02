from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')


class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'role')
        widgets = {
            'role': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['role'].initial = 2


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'role')
        widgets = {
            'role': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['role'].initial = 2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone')

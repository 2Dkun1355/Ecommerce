from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser
from django import forms

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'password1', 'password2']

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control bg-white"}),
            'last_name': forms.TextInput(attrs={'class': "form-control bg-white"}),
            'phone': forms.TextInput(attrs={'class': "form-control bg-white"}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': "form-control bg-white"}),
            'new_password1': forms.PasswordInput(attrs={'class': "form-control bg-white"}),
            'new_password2': forms.PasswordInput(attrs={'class': "form-control bg-white"}),
        }
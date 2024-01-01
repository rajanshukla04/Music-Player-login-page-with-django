# forms.py
from django import forms
from .models import UserProfile
from .models import UserProfile

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'mobile', 'address', 'password']

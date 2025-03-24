from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(required=True)
    birth_date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2025))) 
    
    class Meta:
        model = CustomUser
        fields = ("username", "phone", "birth_date", "password1", "password2")
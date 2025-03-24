import hashlib
import hmac
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'app/home.html')



def register(request):
    if request.method == "POST":
        form  = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect("dashboard") #редирект после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, "app/register.html", {
        "form": form,
        "SOCIALACCOUNT_PROVIDERS": getattr(settings, "SOCIALACCOUNT_PROVIDERS", {})
    })

    

def user_login(request):
    if request.method == "POST":
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "app/login.html", {"form": form})
    

from django.urls import path
from app.views import home, register, user_login
from django.http import HttpResponse

from django.shortcuts import redirect

def google_login_redirect(request):
    return redirect('/accounts/google/login')

urlpatterns = [
    path('', home, name='home'), 
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', lambda request: HttpResponse('<h1>dashboard page in process</h1>'), name='dashboard'),
    
    path('login/', google_login_redirect, name='google_login_redirect'),
]

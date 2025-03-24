from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), # connect to app.urls
    path('accounts/', include('allauth.urls')), # OAuth urls
    
]

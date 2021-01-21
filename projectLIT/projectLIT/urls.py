"""projectLIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),
    path('playlists/', mainapp.playlists, name='playlists'),
    path('playlist/', mainapp.playlist, name='playlist'),
    path('accounts/', mainapp.connected, name='accounts'),
    path('account/', mainapp.account, name='account'),
    path('register/', mainapp.register, name='register'),
    path('signin/', mainapp.signin, name='signin'),
]
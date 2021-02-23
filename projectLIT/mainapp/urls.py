from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('playlists/', mainapp.playlists, name='playlists'),
    path('playlist/', mainapp.playlist, name='playlist'),
    path('accounts/', mainapp.connected, name='accounts'),
    path('account/', mainapp.account, name='account'),
    # path('register/', mainapp.register, name='register'),
    # path('signin/', mainapp.signin, name='signin'),
]
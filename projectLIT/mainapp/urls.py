from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

# urlpatterns = [
#     path('', mainapp.playlists, name='playlists'),
#     path('<int:pk>/', mainapp.playlists, name='playlist')
# ]
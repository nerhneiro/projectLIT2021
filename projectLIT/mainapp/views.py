from django.shortcuts import render
from .models import Album, Artist, Label, Tag
# Create your views here.
def main(request):
    albums = Album.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        log_link = 'auth:logout'
        log_message = 'Log out'
    else:
        username = ''
        log_link = 'auth:login'
        log_message = 'Log in'
    context = {
        'title': 'Main',
        'username': username,
        'log_message': log_message,
        'log_link': log_link,
    }

    return render(request, 'mainapp/index.html', context)


def connected(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ''
    context = {
        'title': 'Connected accounts',
        'username': username,
    }
    return render(request, 'mainapp/connectedaccounts.html', context)


def playlists(request):
    if request.user.is_authenticated:
        albums = request.user.albums.all()
        username = request.user.username
    else:
        albums = []
        username = ''
    context = {
        'title': 'Playlists',
        'albums': albums,
        'username': username
    }
    return render(request, 'mainapp/playlists.html', context)


def account(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ''
    context = {
        'title': 'Account',
        'username': username,
    }
    return render(request, 'mainapp/account.html', context)

#
# def register(request):
#
#     context = {
#         'title': 'Registration'
#     }
#     return render(request, 'mainapp/register.html',context)
#
#
# def signin(request):
#     context = {
#         'title': 'Sign in'
#     }
#     return render(request, 'mainapp/signin.html', context)


def playlist(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ''
    context = {
        'username': username,
    }
    return render(request, 'mainapp/playlist.html', context)
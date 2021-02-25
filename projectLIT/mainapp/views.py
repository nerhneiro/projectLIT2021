from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Album, Artist, Label, Tag
# Create your views here.
def main(request):
    albums = Album.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        log_link = 'auth:logout'
        log_message = 'Log out'
        authenticated = True
    else:
        username = ''
        log_link = 'auth:login'
        log_message = 'Log in'
        authenticated = False
    context = {
        'title': 'Main',
        'username': username,
        'log_message': log_message,
        'log_link': log_link,
        'authenticated': authenticated,
    }
    return render(request, 'mainapp/index.html', context)


def connected(request):
    if request.user.is_authenticated:
        username = request.user.username
        authenticated = True
    else:
        username = ''
        authenticated = False
    context = {
        'title': 'Connected accounts',
        'username': username,
        'authenticated': authenticated,
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
        first_name = request.user.first_name
        last_name = request.user.last_name
        date_joined = request.user.date_joined
        country = request.user.country
        age = request.user.age
        context = {
            'title': 'Account',
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'date_joined': date_joined,
            'country': country,
            'age': age,
        }
        return render(request, 'mainapp/account.html', context)
    else:
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def playlist(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ''
    context = {
        'username': username,
    }
    return render(request, 'mainapp/playlist.html', context)
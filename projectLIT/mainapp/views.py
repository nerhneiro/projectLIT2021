from django.shortcuts import render
from .models import Album, Artist, Label, Tag
# Create your views here.
def main(request):
    albums = Album.objects.all()
    context = {
        'title': 'Main',
        'albums': albums
    }

    return render(request, 'mainapp/index.html', context)


def connected(request):
    context = {
        'title': 'Connected accounts'
    }
    return render(request, 'mainapp/connectedaccounts.html', context)


def playlists(request):
    albums = Album.objects.all()
    context = {
        'title': 'Playlists',
        'albums': albums
    }
    return render(request, 'mainapp/playlists.html', context)


def account(request):
    context = {
        'title': 'Account'
    }
    return render(request, 'mainapp/account.html', context)


def register(request):
    context = {
        'title': 'Registration'
    }
    return render(request, 'mainapp/register.html',context)


def signin(request):
    context = {
        'title': 'Sign in'
    }
    return render(request, 'mainapp/signin.html', context)


def playlist(request):
    return render(request, 'mainapp/playlist.html')
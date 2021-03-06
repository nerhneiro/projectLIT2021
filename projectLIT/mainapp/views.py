from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Album, Artist, Label, Tag, Genre, Style
from yandex_music.client import Client
import authapp.requestsYandexDiscogs as ryd
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
    yandexMusicConnected = False
    if request.user.is_authenticated:
        username = request.user.username
        authenticated = True
        if request.user.emailYM != None and request.user.passwordYM != None:
            yandexMusicConnected = True
    else:
        username = ''
        authenticated = False
    context = {
        'title': 'Connected accounts',
        'username': username,
        'authenticated': authenticated,
        'yandexMusicConnected': yandexMusicConnected,
    }
    return render(request, 'mainapp/connectedaccounts.html', context)


def playlists(request):
    yandexMusicConnected = False
    if request.user.is_authenticated:
        albums = request.user.albums.all()
        username = request.user.username
        if request.user.emailYM != None and request.user.passwordYM != None:
            yandexMusicConnected = True
    else:
        albums = []
        username = ''
    context = {
        'title': 'Playlists',
        'albums': albums,
        'username': username,
        'yandexMusicConnected': yandexMusicConnected,
    }

    return render(request, 'mainapp/playlists.html', context)

def updateDB(request):
    # try:
    user = request.user
    client = Client.from_credentials(user.emailYM, user.passwordYM)
    albums = client.users_likes_albums()
    albumsIdYM = set()
    for al in albums:
        artists = []
        for ar in al['album']['artists']:
            artists.append((ar['name'], ar['id']))
        album = al['album']['title']
        idYM = al['album']['id']
        albumsIdYM.add(idYM)
        try:
            # print(user.albums.all())
            albumExisting = Album.objects.get(idYandex=idYM)
            # print(albumExisting.album_users.all())
            try:
                album = user.albums.get(idYandex=idYM)
            except:
                user.albums.add(albumExisting)
        except:
            year, genres, styles, labels, idDiscogs = ryd.get_info(album, artists)
            albumNew = Album.objects.create(idYandex=idYM, idDiscogs=idDiscogs, name=album, year=year)
            albumNew.save()
            if genres != None:
                for g in genres:
                    try:
                        genre = Genre.objects.get(name=g)
                        albumNew.genres.add(genre)
                    except:
                        genreNew = Genre.objects.create(name=g)
                        genreNew.save()
                        albumNew.genres.add(genreNew)
            if labels != None:
                for l, id in labels:
                    try:
                        label = Label.objects.get(name=l)
                        albumNew.labels.add(label)
                    except:
                        labelNew = Label.objects.create(name=l, idDiscogs=id)
                        labelNew.save()
                        albumNew.labels.add(labelNew)
            if styles != None:
                for s in styles:
                    try:
                        style = Style.objects.get(name=s)
                        albumNew.styles.add(style)
                    except:
                        styleNew = Style.objects.create(name=s)
                        styleNew.save()
                        albumNew.styles.add(styleNew)
            if artists != None:
                for ar, id in artists:
                    try:
                        artist = Artist.objects.get(idDiscogs=id)
                        albumNew.artists.add(artist)
                    except:
                        artistNew = Artist.objects.create(name=ar, idDiscogs=id)
                        artistNew.save()
                        albumNew.artists.add(artistNew)
            albumNew.save()
            user.albums.add(albumNew)
    albumsIdDB = set()
    for i in user.albums.all():
        albumsIdDB.add(i.idYandex)
    albumsRemove1 = albumsIdYM - albumsIdDB
    albumsRemove2 = albumsIdDB - albumsIdYM
    albumsRemove = albumsRemove1.union(albumsRemove2)
    for i in albumsRemove:
        alb = user.albums.get(idYandex=i)
        user.albums.remove(alb)
    # except:
    #     print("ERRRORRRR")
    #     pass
    yandexMusicConnected = False
    if request.user.is_authenticated:
        albums = request.user.albums.all()
        username = request.user.username
        if request.user.emailYM != None and request.user.passwordYM != None:
            yandexMusicConnected = True
    else:
        albums = []
        username = ''
    context = {
        'title': 'Playlists',
        'albums': albums,
        'username': username,
        'yandexMusicConnected': yandexMusicConnected,
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
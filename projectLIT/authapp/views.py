from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import SiteUserLoginForm, SiteUserRegisterForm, SiteUserEditForm, ConnectYandexMusicAccount
from django.contrib import auth
from django.urls import reverse
from yandex_music.client import Client
import authapp.requestsYandexDiscogs as ryd
from mainapp.models import Album, Artist, Label, Tag, Genre, Style

def login(request):
    title = 'вход'
    
    login_form = SiteUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # albums = user.albums.all()
            # print(albums)
            return HttpResponseRedirect(reverse('mainapp:main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponseRedirect(reverse('mainapp:main'))
    else:
        title = 'вход'

        login_form = SiteUserLoginForm(data=request.POST or None)
        if request.method == 'POST' and login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # albums = user.albums.all()
                # print(albums)
                return HttpResponseRedirect(reverse('mainapp:main'))

        content = {'title': title, 'login_form': login_form}
        return render(request, 'authapp/login.html', content)

def register(request):
    title = 'регистрация'
    
    if request.method == 'POST':
        register_form = SiteUserRegisterForm(request.POST, request.FILES)
    
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = SiteUserRegisterForm()
    
    content = {'title': title, 'register_form': register_form}
    
    return render(request, 'authapp/register.html', content)
    
    
def edit(request):
    title = 'редактирование'
    
    if request.method == 'POST':
        edit_form = SiteUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:account'))
    else:
        edit_form = SiteUserEditForm(instance=request.user)
    
    content = {'title': title, 'edit_form': edit_form}
    
    return render(request, 'authapp/edit.html', content)

def connectYM(request):
    title = ''
    message = ''
    #нужна проверка, что еще не указан аккаунт ЯМ. Если он уже есть, нужно выводить предупреждение, что он будет изменен
    #нужна проверка на существование аккаунта
    if request.method == 'POST':
        edit_form = ConnectYandexMusicAccount(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            user = request.user
            client = Client.from_credentials(edit_form.cleaned_data.get('emailYM'), edit_form.cleaned_data.get('passwordYM'))
            albums = client.users_likes_albums()
            for al in albums:
                artists = []
                for ar in al['album']['artists']:
                    artists.append((ar['name'], ar['id']))
                album = al['album']['title']
                idYM = al['album']['id']
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
                    for g in genres:
                        try:
                            genre = Genre.objects.get(name=g)
                            albumNew.genres.add(genre)
                        except:
                            genreNew = Genre.objects.create(name=g)
                            genreNew.save()
                            albumNew.genres.add(genreNew)
                    for l, id in labels:
                        try:
                            label = Label.objects.get(name=l)
                            albumNew.labels.add(label)
                        except:
                            labelNew = Label.objects.create(name=l, idDiscogs=id)
                            labelNew.save()
                            albumNew.labels.add(labelNew)
                    for s in styles:
                        try:
                            style = Style.objects.get(name=s)
                            albumNew.styles.add(style)
                        except:
                            styleNew = Style.objects.create(name=s)
                            styleNew.save()
                            albumNew.styles.add(styleNew)
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
            return HttpResponseRedirect(reverse('mainapp:main'))
    else:
        edit_form = ConnectYandexMusicAccount(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form,
        'message': message,
    }

    return render(request, 'authapp/connectYM.html', content)
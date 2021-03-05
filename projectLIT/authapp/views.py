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
                    artists.append(ar['name'])
                album = al['album']['title']
                year, genres, styles, labels = ryd.get_info(album, artists)
                for g in genres:
                    try:
                        genre = Genre.objects.get(name=g)
                    except:
                        Genre.objects.create(name=g)
                for l, id in labels:
                    try:
                        lable = Label.objects.get(name=l)
                    except:
                        Label.objects.create(name=l, idDiscogs=id)
                for s in styles:
                    try:
                        style = Style.objects.get(name=s)
                    except:
                        Style.objects.create(name=s)
            return HttpResponseRedirect(reverse('mainapp:main'))
    else:
        edit_form = ConnectYandexMusicAccount(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form,
        'message': message,
    }

    return render(request, 'authapp/connectYM.html', content)
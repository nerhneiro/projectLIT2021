from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import SiteUserLoginForm, SiteUserRegisterForm
from django.contrib import auth
from django.urls import reverse
from mainapp.models import Album
from authapp.forms import SiteUserEditForm

def login(request):
    title = 'вход'
    user = None
    login_form = SiteUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            user.albums.objects.add(Album(name='Album1111', ))
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form, 'user': user}
    return render(request, 'authapp/signin.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
    

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
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = SiteUserEditForm(instance=request.user)
    
    content = {'title': title, 'edit_form': edit_form}
    
    return render(request, 'authapp/edit.html', content)
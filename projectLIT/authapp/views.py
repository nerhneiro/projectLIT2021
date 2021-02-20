from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
# Create your views here.
from authapp.forms import SiteUserLoginForm


def login(request):
    title = 'Login'
    login_form = SiteUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active():
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)

def register(request):
    return render(request, 'authapp/register.html')

def edit(request):
    return render(request, 'authapp/edit.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
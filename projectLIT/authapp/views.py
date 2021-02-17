from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'authapp/singin.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .models import Customer, HR, Manager, Courier, Employee
from django.template.context_processors import csrf
from home.context_processors import hasGroup
from django.contrib import messages
from django import forms
from django.contrib.auth.views import LoginView, LogoutView as DjangoLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, UpdateView
# Create your views here.

def WMLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    
    if user is not None:
        WM.login(request, user)
        messages.add_message(request, messages.INFO, 'You have been logged in successfully')
        return HttpResponseRedirect('/home')
    else:
        messages.add_message(request, messages.INFO, 'Invalid username/password')
        return HttpResponseRedirect('/login')


def WMLogout(request):
    

    if request.user.is_authenticated:
        WM.logout(request)
        messages.add_message, messages.INFO, 'You have been logged out'
        return HttpResponseRedirect('/login')
        
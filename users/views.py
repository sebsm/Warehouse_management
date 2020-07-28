from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .models import Customer, HR, Manager, Courier, Employee
from django.template.context_processors import csrf
from home.context_processors import Role
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

@login_required
def Profile(request):
    return render(request, 'users/profile.html')

@login_required

def Register(request):
    if Role(request.self, 'HR'):
        c = {}
        c.update(csrf(request))
        return render(request, 'profiles/register.html')
    else:
        messages.add.message(request, messages.WARNING, 'You are not allowed to do that')
        return HttpResponseRedirect('/home')

@login_required

def Registration(request):
    if Role(request.user, 'HR'):
        username = request.POST.get('username')
        if User.objects.filter(username = username).exists():
            messages.add.message(request, messages.ERROR, 'Chosen username exists')
            return HttpResponseRedirect(request, '/profile/register')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if not password == repeat_password:
            messages.add.message(request, messages.ERROR, 'Different passwords')
            return HttpResponseRedirect(request, '/profile/register')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        if not contact_number.isdigit():
            messages.add.message(request, messages.ERROR, 'This is not a contact number')
            return HttpResponseRedirect(request, '/profile/register')
        address = request.POST.get('address')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        employed_since= request.POST.get('employed_since')
        employee = User.objects.create_user(username = username, password = password, first_name=first_name, last_name=last_name, email=email)
        employee.employee = Employee(contact_number=int(contact_number), address=address, salary=salary, employed_since = employed_since)
        employee.employee.save()
        employee.save()


        group = Group.objects.get(name = 'employee')
        group.user_set.add(employee)
        group.save()


        messages.add_message(request, messages.WARNING, username + 'has been sucesfully registered')
        return HttpResponseRedirect('/home')
    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/home')

"""
Definition of urls for Warehouse_management.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from login_logout.views import WMLogin, WMLogout, WMAuth
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', WMAuth, name= 'login'),
    path('logout/', WMLogout, name='logout'),
    path('admin/', admin.site.urls),
    path('login_logout/', include('login_logout.urls')),
]

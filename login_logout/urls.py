from django.urls import path
from login_logout.views import WMLogin
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns =[
    path('WM',WMLogin)
]

from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'core'


urlpatterns = [
    path('', item_list),
    path('item_list/', item_list, name='item-list'),
    path('checkout/', checkout),
    path('product/', product),
]

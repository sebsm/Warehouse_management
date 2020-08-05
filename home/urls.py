from django.contrib import admin
from django.urls import path, include
from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    add_to_cart
)


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name= 'product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_the_cart/<slug>/', remove_from_the_cart, name='remove-from-the-cart'),
]

"""
Definition of views.
"""

from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
       request,
       'home/home-page.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
       }
   )

# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'home/contact.html',
#         {
#             'title':'Contact',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         }
#     )

# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'home/about.html',
#         {
#             'title':'About',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )

def product(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'home/product.html', context)

def checkout(request):
    return render(request, 'home/checkout.html')



class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home/home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "home/product.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            order.items.add(order.item)
            messages.info(request, "This item was added to your cart")
            return redirect("home:product", slug = slug)
    else:
        ordered_date = timezone.now() 
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item quantity was updated")
        return redirect("home:product", slug = slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order.item)
            messages.info(request, "This item was removed from your cart")
            return redirect("home:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home:product", slug=slug)
    return redirect("home:product", slug=slug)
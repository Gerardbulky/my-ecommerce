from django.shortcuts import render

# Create your views here.

def base(request):
    context = {}
    return render(request, 'ecommerce/base.html', context)

def stores(request):
    context = {}
    return render(request, 'ecommerce/stores.html', context)

def cart(request):
    context = {}
    return render(request, 'ecommerce/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'ecommerce/checkout.html', context)

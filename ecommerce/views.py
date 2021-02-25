from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order, OrderItem, ShippingAddress

# Create your views here.


def base(request):
    context = {}
    return render(request, 'ecommerce/base.html', context)


def stores(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'ecommerce/stores.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'ecommerce/product_detail.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []  

    context = {'items': items, 'order': order}
    return render(request, 'ecommerce/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'ecommerce/checkout.html', context)


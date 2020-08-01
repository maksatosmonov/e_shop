from django.shortcuts import render
from product.models import *
from product.forms import *
from django.db.models import Q



def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")  
        products = Product.objects.filter(
                Q(active=True), 
                Q(deleted=False),
                Q(name__contains=key) | 
                Q(description__contains=key) | 
                Q(category__name__contains=key))
        
    else:
        products = Product.objects.filter(active=True, deleted=False)

    return render(
                request,
                "product/products.html", 
                 {"products": products})

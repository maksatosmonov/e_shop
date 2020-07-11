from django.shortcuts import render
from product.models import *
from django.contrib.auth.models import User



def products(request):
    context = {}
    context["products"] = Product.objects.filter(active=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)



# Create your views here.

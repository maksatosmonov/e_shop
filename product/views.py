from django.shortcuts import render, HttpResponse
from product.models import *
from django.contrib.auth.models import User



def products(request):
    context = {}
    context["products_all"] = Products.objects.all()
    return render(request, "products/products.html", context)



# Create your views here.

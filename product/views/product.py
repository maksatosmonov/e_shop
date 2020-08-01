from django.shortcuts import render
from product.models import *
from product.forms import *


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)

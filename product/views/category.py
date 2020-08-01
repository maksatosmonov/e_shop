
from django.shortcuts import render
from django.urls import reverse
from product.models import *



def category(request, pk):
    context = {}
    context["products"] = Product.objects.filter(
        category__id=pk,
        avialable=True,
        deleted=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)
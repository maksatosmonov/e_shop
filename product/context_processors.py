  
from product.models import Category
from django.shortcuts import render

def category(request):
    context = {}
    context["categories"] = Category.objects.order_by("name")
    return context

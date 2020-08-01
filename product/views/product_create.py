from django.shortcuts import render
from product.models import *
from product.forms import *
from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            return render(request, "product/success.html")

    context = {}
    context["form"] = ProductForm()

    return render(request, "product/create.html", context)
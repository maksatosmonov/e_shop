from django.shortcuts import render, redirect
from product.models import *
from product.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect("home")

    context = {}    
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return render(request, "product/success.html")

    
    context["form"] = ProductForm(instance=product)

    return render(request, "product/form.html", context)
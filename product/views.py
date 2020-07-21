from django.shortcuts import render, redirect
from product.models import *
from product.forms import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test


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


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


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

    return render(request, "product/form.html", context)

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


@login_required(login_url="/login/")
def product_delete(request, id):
    product = Product.objects.get(id=id)
    if product.user != request.user:
        return redirect("home")
    else:
        product.deleted = True 
        product.save()
        return render(request, "product/success.html")



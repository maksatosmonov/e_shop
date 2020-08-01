from django.shortcuts import render, redirect
from product.models import *
from product.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def product_delete(request, id):
    product = Product.objects.get(id=id)
    if product.user != request.user:
        return redirect("home")
    else:
        product.deleted = True 
        product.save()
        return render(request, "product/success.html")



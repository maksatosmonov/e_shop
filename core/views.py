from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from core.forms import *
from product.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


def home(request):
    return redirect("products")

def test(request):
    return HttpResponse("test")


def login(request):
    context = {}
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if  form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)

    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)

def logout(request):
    auth.logout(request)
    return redirect("home")


def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if form.is_valid():
            form.save()
            return redirect("login")

    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)


def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    return render(request, "core/profile.html", context)


def retailers(request):
    retailers = User.objects.exclude(product=None)
    context = {"retailers":retailers}
    return render(request, "core/retailers.html", context)


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return render(request, "core/success.html")
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "core/password_change.html", {"form": form})





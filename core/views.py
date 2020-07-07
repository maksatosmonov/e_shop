from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("homepage Maksat")


def test(request):
    return HttpResponse("test")

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User


def retailers(request):
    retailers = User.objects.exclude(product=None)
    context = {"retailers":retailers}
    return render(request, "core/retailers.html", context)
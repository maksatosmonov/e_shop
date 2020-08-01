from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .user_not_authenticated import user_not_authenticated


# @require_http_methods(["GET"])
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




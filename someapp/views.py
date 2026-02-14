from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def main_page(request):
    return render(request, 'main.html')

@login_required
def cabinet_view(request):
    return render(request, 'kab.html')

def logout_view(request):
    logout(request)
    return redirect('main')
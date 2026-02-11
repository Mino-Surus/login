from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def main_page(request):
    return render(request, 'main.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST['username']
        user, _ = User.objects.get_or_create(username=name)
        login(request, user)
        return redirect('main')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('main')
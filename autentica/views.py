from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('home')
        else:
            messages.success(request, ('Error en la autentificación'))
            return redirect('login_user')
            
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')
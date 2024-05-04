from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm

def loginuser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeapp:dashboard')
        else:
            messages.success(request, ("The username or the password are incorrect"))
            # return redirect('signin')
            return render(request, 'login.html' ,{})
    else:
        return render(request, 'login.html' ,{})
    
def logoutuser(request):
    logout(request)
    messages.success(request, ("You have logout"))
    return redirect('homeapp:dashboard')

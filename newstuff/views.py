from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from logins_and_alerts.models import Drone, User

def dashboard(request):   
    user_list = User.objects.all()  
    drone_list = Drone.objects.all()
    drone_active = 0
    drone_not_active = 0
    for drone in drone_list:
        if drone.active:
            drone_active = drone_active + 1
        else:
            drone_not_active = drone_not_active + 1
    # User_instance = User.objects.create(user=current_user)
    return render(request, 'home.html', {'drone_active': drone_active, 'drone_not_active': drone_not_active, 'drone_list': drone_list, 'user_list': user_list})

def template(request):
    user_list = User.objects.all()  
    return render(request, "empty.html", {'user_list': user_list})

def drones(request):
    user_list = User.objects.all()  
    drone_list = Drone.objects.all()
    
    return render(request, "drones.html", {'drone_list': drone_list, 'user_list': user_list})

def alerts(request):
    user_list = User.objects.all()  
    return render(request, "alerts.html", {'user_list': user_list})

def reports(request):
    user_list = User.objects.all()  
    return render(request, "reports.html", {'user_list': user_list})

def team(request):
    user_list = User.objects.all()  
    return render(request, "team.html", {'user_list': user_list})

def settings(request):
    user_list = User.objects.all()  
    return render(request, "settings.html", {'user_list': user_list})                 
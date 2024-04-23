from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def dashboard(request):
    return render(request, 'home.html')

def template(request):
    return render(request, "empty.html")

def drones(request):
    return render(request, "drones.html")

def alerts(request):
    return render(request, "alerts.html")

def reports(request):
    return render(request, "reports.html")

def team(request):
    return render(request, "team.html")

def settings(request):
    return render(request, "settings.html")
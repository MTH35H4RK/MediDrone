from django.urls import path,include

from . import views

app_name = 'homeapp' 
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("template/", views.template, name="template"),
    path("alerts/", views.alerts, name="alerts"),
    path("reports/", views.reports, name="reports"),
    path("team/", views.team, name="team"),
    path("settings/", views.settings, name="settings"),
    path("drones/", views.drones, name="drones"),
] 
from importlib.resources import path
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="home"),
    path('map/',views.mapPage,name="map"),
    path('report/',views.reportIncident,name="report"),
]

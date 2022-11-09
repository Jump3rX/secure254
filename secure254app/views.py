from django.contrib import messages
from django.shortcuts import render,redirect
import folium
import geocoder
from .models import Report
from secure254app.forms import ReportForm

def index(request):

    return render(request,"base/home.html") 

def mapPage(request):
    incidents = Report.objects.all() #Gets all incidences recorded from the database
    maper = folium.Map(location=[0.0236,37.9062],zoom_start=7,tiles='OpenStreetMap')#Initializes map to a specific country
    for data in incidents:
        lat = data.latitude
        long = data.longitude
        lat = data.latitude
        county = data.county
        area = data.area
        crime = data.incident
        date = data.occurence_date
        confirmed = data.verified
        folium.Marker(location=[lat,long],
        popup=f"County:{county} Incident:{crime} Occured on:{date} Verified:{confirmed}",tooltip=f'Area:{area}',
        icon=folium.Icon(icon='exclamation-triangle',color=color(confirmed),prefix='fa')).add_to(maper)    
    map1 = maper._repr_html_()
    context = {
        'map1':map1
    }
    return render(request,"base/map.html",context) 

def reportIncident(request):
    form = ReportForm()#Creating an instance of the form
    if request.method == 'POST':
        #Checking if a user has entered the correct data in the form.
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Report Sent! Thank you!")
        else:
            messages.info(request,"Check details and try again!")
    context = {'form':form}

    return render(request,"base/report.html",context) 

def color(confirmed):
    if confirmed == True:
        return 'green'
    else:
        return 'red'

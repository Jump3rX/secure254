from django.db import models
import geocoder
from django.utils import timezone
from datetime import date

# Create your models here.
class Report(models.Model):
    COUNTY = [
        ('Mombasa','Mombasa'),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('TanaRiver','TanaRiver'),
        ('Lamu','Lamu'),
        ('TaitaTaveta','TaitaTaveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Isiolo','Isiolo'),
        ('Meru','Meru'),
        ('Tharaka-Nithi','Tharaka-Nithi'),
        ('Embu','Embu'),
        ('Kitui','Kitui'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Nyandarua','Nyandarua'),
        ('Nyeri','Nyeri'),
        ('Kirinyaga','Kirinyaga'),
        ('Muranga','Muranga'),
        ('Kiambu','Kiambu'),
        ('Turkana','Turkana'),
        ('West-Pokot','West-Pokot'),
        ('Samburu','Samburu'),
        ('TransNzoia','TransNzoia'),
        ('UasinGishu','UasinGishu'),
        ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo','Baringo'),
        ('Laikipia','Laikipia'),
        ('Nakuru','Nakuru'),
        ('Narok','Narok'),
        ('Kajiado','Kajiado'),
        ('Kericho','Kericho'),
        ('Bomet','Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga','Vihiga'),
        ('Bungoma','Bungoma'),
        ('Busia','Busia'),
        ('Siaya','Siaya'),
        ('Kisumu','Kisumu'),
        ('HomaBay','HomaBay'),
        ('Migori','Migori'),
        ('Kisii','Kisii'),
        ('Nyamira','Nyamira'),
        ('Nairobi','Nairobi'),
    ]
    INCIDENCES = [
        ('Theft','Theft'),
        ('Robbery','Robbery'),
        ('CarJack','CarJack'),
        ('Fire','Fire'),
        ('Road Accident','Road Accident'),
        ('Hit and Run','Hit and Run'),
        ('Dangerous Driving','Dangerous Driving'),
        ('Traffic Jam','Traffic Jam'),
        ('Other','Other'),
    ]
    
    county= models.CharField(max_length=18,choices=COUNTY,default='Nairobi',null=False)
    area = models.CharField(max_length=200,null=False)
    incident = models.CharField(max_length=25,choices=INCIDENCES,null=False)
    Describe_other_incident = models.TextField(max_length=150,null=True,blank=True)
    occurence_date = models.DateField(default=timezone.now,null=False,blank=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    verified = models.BooleanField(default=False)

    #Converts the name of a location into lat and long coordinates using geocoder then saves it
    def save(self,*args, **kwargs):
        place = self.area
        place_county = self.county
        self.latitude = geocoder.osm(f"{place},{place_county},Kenya").lat
        self.longitude = geocoder.osm(f"{place},{place_county},Kenya").lng
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.county
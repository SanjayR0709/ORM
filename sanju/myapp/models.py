
from django.db import models
from django.contrib import admin
class Service_DB(models.Model):
    Bike_No=models.IntegerField()
    Bike_Name=models.CharField(max_length=10)
    Address=models.TextField()
    Date_Of_Registration=models.DateField()
    Mobile_No=models.IntegerField()
    Warranty=models.CharField()
    Date_Of_Leaving=models.CharField()
class Service_DBAdmin(admin.ModelAdmin):
    list_display=["Bike_No","Bike_Name","Address","Date_Of_Registration","Mobile_No","Warranty","Date_Of_Leaving"]




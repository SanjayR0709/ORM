# Ex02 Django ORM Web Application
## Date: 06.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py


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

admin.py
from django.contrib import admin
from .models import Service_DB,Service_DBAdmin
admin.site.register(Service_DB,Service_DBAdmin)

```


## OUTPUT
![alt text](image.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully

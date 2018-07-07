from django.contrib import admin
from .models import MessagesFromContactUs, Bike, BikeImages

# Register your models here.

admin.site.register((MessagesFromContactUs, Bike, BikeImages))

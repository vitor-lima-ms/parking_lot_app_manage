from django.contrib import admin
from .models import Autos, ParkingSpace

# Register your models here.

@admin.register(Autos)
class AutosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'autos_plate',
        'checkin_date',
        'checkin_time',
    ]

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'occupied',
        'occupied_by',
    ]
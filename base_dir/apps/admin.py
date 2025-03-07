from django.contrib import admin
from .models import Autos, ParkingSpace, Driver

# Register your models here.

@admin.register(Autos)
class AutosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'autos_plate',
        'checkin_datetime',
    ]

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'occupied',
        'occupied_by',
    ]

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = [
        'driver_name',
        'cnh',
        'cpf'
    ]

    class Meta:
        ordering = (('driver_name'))
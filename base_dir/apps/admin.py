from django.contrib import admin
from .models import Car, CarSpace

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'model',
        'car_plate',
        'checkin_date',
        'checkin_time',
    ]

@admin.register(CarSpace)
class CarSpaceAdmin(admin.ModelAdmin):
    list_display = [
        'occupied',
        'occupied_by',
    ]
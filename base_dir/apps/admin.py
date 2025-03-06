from django.contrib import admin
from .models import Automobile, AutomobileSpace

# Register your models here.

@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):
    list_display = [
        'model',
        'automobile_plate',
        'checkin_date',
        'checkin_time',
    ]

@admin.register(AutomobileSpace)
class AutomobileSpaceAdmin(admin.ModelAdmin):
    list_display = [
        'occupied',
        'occupied_by',
    ]
from django import forms
from .models import Autos, ParkingSpace, Driver

"""Allows you to create new parking spaces"""
CHOICES_LIST = list()
for i in range(101):
    CHOICES_LIST.append((i, str(i)))

class ParkingSpaceCreationForm(forms.Form):
    qtd = forms.TypedChoiceField(choices=CHOICES_LIST, coerce=int)

"""Form to create instances of the Driver model"""
class DriverRegisterForm(forms.Form):
    driver_name = forms.CharField(max_length=50)
    monthly = forms.BooleanField(required=False)
    cnh = forms.CharField(max_length=11)
    cpf = forms.CharField(max_length=11)
    file_upload = forms.FileField(required=False)

"""Form to create instances of the Autos model and assign drivers"""
class AutosRegisterForm(forms.Form):
    driver_name = forms.ModelChoiceField(
        Driver.objects.all(),
        to_field_name='driver_name'
    )
    model = forms.CharField(max_length=50)
    autos_plate = forms.CharField(max_length=7)

"""Form to assign autos to parking spaces"""
class ParkingAssignmentForm(forms.Form):
    parking_places = forms.ModelChoiceField(
        ParkingSpace.objects.filter(occupied=False)
    )
    occupied = forms.BooleanField()
    occupied_by = forms.ModelChoiceField(
        Autos.objects.filter(parked=False),
        to_field_name='model'
    )
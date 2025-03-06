from django import forms
from .models import Autos

"""Allows you to create new parking spaces"""
CHOICES_LIST = list()
for i in range(101):
    CHOICES_LIST.append((i, str(i)))

class ParkingSpaceCreationForm(forms.Form):
    qtd = forms.TypedChoiceField(choices=CHOICES_LIST, coerce=int)

"""Form to create instances of the Autos model"""
class AutosRegisterForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = [
            'model',
            'autos_plate',
        ]
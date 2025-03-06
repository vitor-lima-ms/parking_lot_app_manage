from django.views.generic.edit import FormView
from .forms import ParkingSpaceCreationForm, AutosRegisterForm
from .models import Autos, ParkingSpace
from django.shortcuts import render, redirect

# Create your views here.


"""View that allows you to add new parking spaces"""
class ParkingSpaceCreationFormView(FormView):
    template_name = 'parking_creation_form.html'
    form_class = ParkingSpaceCreationForm

"""Main view. Here we see all the unoccupied parking spaces"""
def main_page(request):
    form = ParkingSpaceCreationForm(request.POST)

    if form.is_valid():
        for i in range(form.cleaned_data['qtd']):
           ParkingSpace.objects.create()

    all_parking_spaces = ParkingSpace.objects.all()
    
    return render(request, 'main_page.html', {'all_parking_spaces': all_parking_spaces})


class AutosFormView(FormView):
    template_name = 'autos_form.html'
    form_class = AutosRegisterForm

def autos_register(request):
    form = AutosRegisterForm(request.POST)

    if form.is_valid():
        autos = form.save()
    
    return render(request, 'autos_register.html', {'autos': autos})
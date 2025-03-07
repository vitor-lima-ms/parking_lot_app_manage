from django.views.generic.edit import FormView
from .forms import ParkingSpaceCreationForm, DriverRegisterForm, AutosRegisterForm, ParkingAssignmentForm
from .models import Autos, ParkingSpace, Driver
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime, timezone
from .functions import price_calculator

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

    unoccupied_parking_spaces = ParkingSpace.objects.filter(occupied=False)
    
    return render(request, 'main_page.html', {'unoccupied_parking_spaces': unoccupied_parking_spaces})

"""View that allows create instances of Driver"""
class DriverRegisterFormView(FormView):
    template_name = 'driver_register_form.html'
    form_class = DriverRegisterForm

def saving_driver(request):    
    form = DriverRegisterForm(request.POST)
    
    if form.is_valid():
        driver = Driver.objects.create(
            driver_name=form.cleaned_data['driver_name'],
            monthly=form.cleaned_data['monthly'],
            cnh=form.cleaned_data['cnh'],
            cpf=form.cleaned_data['cpf'],
            file_upload=form.cleaned_data['file_upload']
        )
        driver.save()
        
    return redirect('apps:autos_register_form')

"""View that allows create instances of Autos and assign drivers"""
class AutosRegisterFormView(FormView):
    template_name = 'autos_register_form.html'
    form_class = AutosRegisterForm

def saving_autos(request):
    form = AutosRegisterForm(request.POST)
    
    if form.is_valid():
        Autos.objects.create(
            driver_name=form.cleaned_data['driver_name'],
            model=form.cleaned_data['model'],
            autos_plate=form.cleaned_data['autos_plate'],
        )
    
    return redirect('apps:parking_assignment')

"""View that allows assign autos to parking spaces"""
class ParkingAssignmentFormView(FormView):
    template_name = 'parking_assignment_form.html'
    form_class = ParkingAssignmentForm

def saving_parking_place(request):
    form = ParkingAssignmentForm(request.POST)

    if form.is_valid():
        parking_space = get_object_or_404(ParkingSpace, id=form.cleaned_data['parking_places'].id)
        parking_space.occupied = True
        parking_space.occupied_by = form.cleaned_data['occupied_by']
        parking_space.save()

        auto = get_object_or_404(Autos, model=form.cleaned_data['occupied_by'].model)
        auto.parked = True
        auto.save()
    
    return redirect('apps:main_page')

"""Here we see all the occupied parking spaces"""
def occupied_parking_spaces(request):
    occupied_parking_spaces = ParkingSpace.objects.filter(occupied=True)

    return render(request, 'occupied_parking_spaces.html', {'occupied_parking_spaces': occupied_parking_spaces})

def registered_drivers(request):
    all_registered_drivers = Driver.objects.all()

    return render(request, 'registered_drivers.html', {
        'all_registered_drivers': all_registered_drivers,
    })

"""In this view, we calculate the amount to be paid and see all relevant information before receiving payment and releasing the parking space"""
def pre_finish(request, parking_space_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)
    
    checkin_datetime = parking_space.occupied_by.checkin_datetime
    current_datetime = datetime.now(timezone.utc)

    time_delta = current_datetime - checkin_datetime

    price = round(price_calculator(time_delta), 2)

    fmt_price = f'{price:.2f}'.replace('.', ',')

    return render(request, 'pre_finish.html', {
        'parking_space': parking_space,
        'checkin_datetime': checkin_datetime,
        'current_datetime': current_datetime,
        'price': fmt_price,
    })

def finish(request, parking_space_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)

    parking_space.remove_auto(parking_space.occupied_by)
    parking_space.save()

    return redirect('apps:main_page')
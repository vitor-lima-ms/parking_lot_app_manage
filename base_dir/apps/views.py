from django.views.generic.edit import FormView
from .forms import ParkingSpaceCreationForm, DriverRegisterForm, AutosRegisterForm, ParkingAssignmentForm
from .models import Autos, ParkingSpace, Driver
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
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

"""View that allows you to view the occupancy history of a parking space"""
def parking_space_history(request, parking_space_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)

    return render(request, 'parking_space_history.html', {'history': parking_space.history})

"""View that allows create instances of Driver"""
class DriverRegisterFormView(FormView):
    template_name = 'driver_register_form.html'
    form_class = DriverRegisterForm

def saving_driver(request):    
    form = DriverRegisterForm(request.POST)
    
    if form.is_valid():
        try:
            drivers = get_list_or_404(Driver, cpf=form.cleaned_data['cpf'])
            if len(drivers) >= 1:
                return render(request, 'driver_register_form.html', {'error': 'Motorista já cadastrado!'})
        except:
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
        try:
            autos = get_list_or_404(Autos, autos_plate=form.cleaned_data['autos_plate'])
            if len(autos) >= 1:
                return render(request, 'autos_register_form.html', {'error': 'Automóvel já cadastrado!'})
        except:
            Autos.objects.create(
                driver=form.cleaned_data['driver_doc'],
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
        
        auto = get_object_or_404(Autos, autos_plate=form.cleaned_data['occupied_by'].autos_plate)
        auto.parked = True
        auto.save()
    
    return redirect('apps:main_page')

"""Here we see all the occupied parking spaces"""
def occupied_parking_spaces(request):
    occupied_parking_spaces = ParkingSpace.objects.filter(occupied=True)

    return render(request, 'occupied_parking_spaces.html', {'occupied_parking_spaces': occupied_parking_spaces})

"""Here we see all registered drivers"""
def registered_drivers(request):
    all_registered_drivers = Driver.objects.all()

    return render(request, 'registered_drivers.html', {
        'all_registered_drivers': all_registered_drivers,
    })

"""Here we see all registered autos"""
def registered_autos(request):
    all_registered_autos = Autos.objects.all()

    return render(request, 'registered_autos.html', {
        'all_registered_autos': all_registered_autos,
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

def finish(request, parking_space_id, autos_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)
    autos = get_object_or_404(Autos, id=autos_id)

    parking_space.add_history()
    parking_space.remove_auto()
    autos.parked = False
    autos.save()
    parking_space.save()

    return redirect('apps:main_page')
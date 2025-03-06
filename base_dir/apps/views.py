from django.views.generic.edit import FormView
from .forms import ParkingSpaceCreationForm, AutosRegisterForm
from .models import ParkingSpace
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

"""View that allows create instances of Autos"""
class AutosRegisterFormView(FormView):
    template_name = 'autos_register_form.html'
    form_class = AutosRegisterForm

"""View that allows assign autos to parking spaces"""
def assign_autos_to_parking_space(request):
    form = AutosRegisterForm(request.POST)
    if form.is_valid():
        auto = form.save()

    unoccupied_parking_spaces = ParkingSpace.objects.filter(occupied=False)
    parking_space = unoccupied_parking_spaces[0]

    parking_space.add_auto(auto)
    parking_space.save()

    return redirect('apps:occupied_parking_spaces')

"""Here we see all the occupied parking spaces"""
def occupied_parking_spaces(request):
    occupied_parking_spaces = ParkingSpace.objects.filter(occupied=True)

    return render(request, 'occupied_parking_spaces.html', {'occupied_parking_spaces': occupied_parking_spaces})

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

    parking_space.remove_auto()
    parking_space.save()

    return redirect('apps:main_page')
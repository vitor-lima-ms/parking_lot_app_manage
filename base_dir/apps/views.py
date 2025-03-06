from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import CarForm
from .models import Car, CarSpace

# Create your views here.

class CarFormView(FormView):
    template_name = 'car_form.html'
    form_class = CarForm

def car_register(request):
    form = CarForm(request.POST)

    if form.is_valid():
        car = form.save()
    
    return render(request, 'car_register.html', {'car': car})
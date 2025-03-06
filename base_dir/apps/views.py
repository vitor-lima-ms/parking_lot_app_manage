from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AutomobileForm
from .models import Automobile, AutomobileSpace

# Create your views here.

class AutomobileFormView(FormView):
    template_name = 'automobile_form.html'
    form_class = AutomobileForm

def automobile_register(request):
    form = AutomobileForm(request.POST)

    if form.is_valid():
        automobile = form.save()
    
    return render(request, 'automobile_register.html', {'automobile': automobile})
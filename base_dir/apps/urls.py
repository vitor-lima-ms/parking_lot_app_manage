from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('car_form/', views.CarFormView.as_view(), name='car_form'),
    path('car_register/', views.car_register, name='car_register'),
]
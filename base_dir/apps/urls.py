from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('parking_creation_form/', views.ParkingSpaceCreationFormView.as_view(), name='parking_creation_form'),
    path('autos_register_form/', views.ParkingSpaceCreationFormView.as_view(), name='parking_creation_form'),
    path('', views.main_page, name='main_page'),
]
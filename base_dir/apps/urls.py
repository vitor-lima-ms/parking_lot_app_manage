from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('parking_creation_form/', views.ParkingSpaceCreationFormView.as_view(), name='parking_creation_form'),

    path('parking_space_history/<int:parking_space_id>', views.parking_space_history, name='parking_space_history'),

    path('driver_register_form/', views.DriverRegisterFormView.as_view(), name='driver_register_form'),

    path('saving_driver/', views.saving_driver, name='saving_driver'),

    path('autos_register_form/', views.AutosRegisterFormView.as_view(), name='autos_register_form'),

    path('saving_autos/', views.saving_autos, name='saving_autos'),

    path('parking_assignment_form/', views.ParkingAssignmentFormView.as_view(), name='parking_assignment_form'),

    path('saving_parking_place/', views.saving_parking_place, name='saving_parking_place'),

    path('occupied_parking_spaces/', views.occupied_parking_spaces, name='occupied_parking_spaces'),

    path('registered_drivers/', views.registered_drivers, name='registered_drivers'),
    
    path('driver_search/', views.driver_search, name='driver_search'),

    path('registered_autos/', views.registered_autos, name='registered_autos'),

    path('plate_search/', views.plate_search, name='plate_search'),

    path('pre_finish/<int:parking_space_id>', views.pre_finish, name='pre_finish'),

    path('finish/<int:parking_space_id>/<int:autos_id>', views.finish, name='finish'),
    
    path('', views.main_page, name='main_page'),
]
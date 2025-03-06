from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('parking_creation_form/', views.ParkingSpaceCreationFormView.as_view(), name='parking_creation_form'),

    path('autos_register_form/', views.AutosRegisterFormView.as_view(), name='autos_register_form'),

    path('parking_assignment/', views.assign_autos_to_parking_space, name='parking_assignment'),

    path('occupied_parking_spaces/', views.occupied_parking_spaces, name='occupied_parking_spaces'),

    path('pre_finish/<int:parking_space_id>', views.pre_finish, name='pre_finish'),

    path('finish/<int:parking_space_id>', views.finish, name='finish'),
    
    path('', views.main_page, name='main_page'),
]
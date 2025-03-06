from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('automobile_form/', views.AutomobileFormView.as_view(), name='automobile_form'),
    path('automobile_register/', views.automobile_register, name='automobile_register'),
]
from django.db import models
from datetime import datetime, timezone

# Create your models here.

"""Model representing drivers"""
class Driver(models.Model):
    driver_name = models.CharField(max_length=50)
    monthly = models.BooleanField(default=False)
    cnh = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    file_upload = models.FileField(upload_to='uploaded_files', blank=True)

    def __str__(self):
        return f'{self.driver_name} - {self.cpf}'

"""Model representing automobiles"""
class Autos(models.Model):
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        default=None
    )
    model = models.CharField(max_length=50)
    autos_plate = models.CharField(max_length=7)
    checkin_datetime = models.DateTimeField(auto_now=True)
    parked = models.BooleanField(default=False)

    class Meta:
        ordering = (('-checkin_datetime',))
        verbose_name = 'Autos'
        verbose_name_plural = 'Autos'
    
    def __str__(self):
        return f'{self.model} - {self.autos_plate}'

"""Model representing parking spaces"""
class ParkingSpace(models.Model):
    occupied = models.BooleanField(default=False)
    occupied_by = models.OneToOneField(
        Autos,
        null=True,
        default=None,
        on_delete=models.SET_NULL       
    )
    def create_list():
        return list({})

    history = models.JSONField(default=create_list, null=True)

    def __str__(self):
        return f'Vaga {self.id}'
    
    """Function to remove a veichle in a parking space"""
    def remove_auto(self):
        self.occupied = False
        self.occupied_by = None
    
    """Function to create the history of the parking space"""
    def add_history(self):
        current_datetime = datetime.now(timezone.utc)
        occupied_by = self.occupied_by
        autos_plate = self.occupied_by.autos_plate
        checkin_datetime = self.occupied_by.checkin_datetime
        
        self.history.append({
            'model': str(occupied_by),
            'autos_plate': str(autos_plate),
            'checkin_datetime': str(checkin_datetime),
            'checkout_datetime': str(current_datetime)
        })
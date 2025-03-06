from django.db import models

# Create your models here.

"""Model representing automobiles"""
class Autos(models.Model):
    driver_name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    autos_plate = models.CharField(max_length=7)
    checkin_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (('-checkin_datetime',))
        verbose_name = 'Autos'
        verbose_name_plural = 'Autos'
    
    def __str__(self):
        return f'{self.model} {self.autos_plate}'

"""Model representing parking spaces"""
class ParkingSpace(models.Model):
    occupied = models.BooleanField(default=False)
    occupied_by = models.OneToOneField(
        Autos,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='parking_space'        
    )

    def __str__(self):
        return f'Vaga {self.id}, {self.occupied}, {self.occupied_by}'
    
    """Function to add a veichle in a parking space"""
    def add_auto(self, auto):
        self.occupied = True
        self.occupied_by = auto
    
    """Function to remove a veichle in a parking space"""
    def remove_auto(self):
        self.occupied = False
        self.occupied_by = None
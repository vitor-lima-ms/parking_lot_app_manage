from django.db import models

# Create your models here.

"""Model representing automobiles"""
class Autos(models.Model):
    model = models.CharField(max_length=50)
    autos_plate = models.CharField(max_length=7)
    checkin_date = models.DateField(auto_now_add=True)
    checkin_time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = (('-checkin_time',))
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
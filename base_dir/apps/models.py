from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=50)
    car_plate = models.CharField(max_length=7)
    checkin_date = models.DateField(auto_now_add=True)
    checkin_time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = (('-checkin_time'),)

    def __str__(self):
        return f'{self.model} {self.car_plate}'

class CarSpace(models.Model):
    occupied = models.BooleanField(default=False)
    occupied_by = models.OneToOneField(
        Car,
        related_name='car_space',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'Vaga {self.id}'
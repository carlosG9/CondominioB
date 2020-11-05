from django.db import models
import uuid
from django.urls import reverse


class visits (models.Model):
    rut = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tower = models.CharField(max_length=1)
    department = models.CharField(max_length=10)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} ({self.last_name})'


class salon(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    fecha = models.DateField()
    salon = models.CharField(max_length=15)

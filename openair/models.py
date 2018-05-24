from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mac_address = models.CharField(max_length=17, unique=True)
    ip_address = models.CharField(max_length=15, unique=True)
    enum = models.PositiveSmallIntegerField(unique=True)
    active = models.BooleanField()

    def __str__(self):
        return self.name
        
class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=4, unique=True)
    enum = models.PositiveSmallIntegerField(unique=True)
    active = models.BooleanField()

    def __str__(self):
        return self.name
        
class Survey(models.Model):
    inserted = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamp = models.PositiveIntegerField()
    device = models.ForeignKey(Device, models.CASCADE)
    sensor = models.ForeignKey(Sensor, models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return str(self.inserted)
        
class Error(models.Model):
    inserted = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamp = models.PositiveIntegerField()
    device = models.ForeignKey(Device, models.CASCADE)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.inserted)
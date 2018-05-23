from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=17)
    ip_address = models.CharField(max_length=15)
    active = models.BooleanField()

    def __str__(self):
        return self.name
        
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    code = models.PositiveSmallIntegerField()
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
        return self.pk
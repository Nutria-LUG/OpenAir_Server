from django.contrib import admin
from .models import Device,Sensor,Survey

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'mac_address', 'ip_address', 'active']
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'active']
    
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'inserted', 'timestamp', 'device', 'sensor', 'value']

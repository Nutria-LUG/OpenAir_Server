from datetime import datetime
from django.contrib import admin
from .models import Device,Sensor,Survey,Error

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'mac_address', 'ip_address', 'enum', 'active']
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'enum', 'active']
    
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['inserted', 'converted_timestamp', 'device', 'sensor', 'value']

    def converted_timestamp(self, obj):
        return datetime.fromtimestamp(obj.timestamp)
    converted_timestamp.short_description = 'Timestamp'
    
@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ['inserted', 'timestamp', 'device', 'message']

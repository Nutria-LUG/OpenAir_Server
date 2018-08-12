from datetime import datetime
from django.contrib import admin
from .models import Device,Sensor,Survey,Error

# Register your models here.
class TimestampAdmin(admin.ModelAdmin):
    def converted_timestamp(self, obj):
        return datetime.fromtimestamp(obj.timestamp)
    converted_timestamp.short_description = 'Timestamp'

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'mac_address', 'ip_address', 'enum', 'active']
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'enum', 'active']
    
@admin.register(Survey)
class SurveyAdmin(TimestampAdmin):
    list_display = ['inserted', 'converted_timestamp', 'device', 'sensor', 'value']
    list_filter = ['inserted', 'device', 'sensor']
    
@admin.register(Error)
class ErrorAdmin(TimestampAdmin):
    list_display = ['inserted', 'converted_timestamp', 'device', 'message']

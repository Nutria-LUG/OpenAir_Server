from rest_framework import serializers
from ..models import Device, Survey, Error

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'mac_address', 'ip_address', 'enum']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['timestamp', 'device', 'sensor', 'value']

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['timestamp', 'device', 'message']
from rest_framework import serializers
from ..models import Survey, Error

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['timestamp', 'device', 'sensor', 'value']

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['timestamp', 'device', 'message']
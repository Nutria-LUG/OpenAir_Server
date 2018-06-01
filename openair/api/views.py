from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import DevicePermission
from .serializers import SurveySerializer, ErrorSerializer
from .utils import get_request_data, set_device_to_data, set_sensor_to_data
from ..models import Survey, Error

@api_view(['POST'])
@permission_classes([DevicePermission])
def survey(request):
    data = get_request_data(request)
    data = set_device_to_data(data, request)
    data = set_sensor_to_data(data)
    serializer = SurveySerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([DevicePermission])
def error(request):
    data = get_request_data(request)
    data = set_device_to_data(data, request)
    serializer = ErrorSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
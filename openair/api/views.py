from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import DevicePermission
from .serializers import SurveySerializer, ErrorSerializer
from .utils import set_device_by_request, set_sensor_by_request
from ..models import Survey, Error

@api_view(['POST'])
@permission_classes([DevicePermission])
def survey(request):
    data = request.data
    data = set_device_by_request(request)
    data = set_sensor_by_request(request)
    serializer = SurveySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([DevicePermission])
def error(request):
    data = request.data
    data = set_device_by_request(request)
    serializer = ErrorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
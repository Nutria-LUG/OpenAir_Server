from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import DeviceRegistrationPermission, DeviceRestrictionPermission
from .serializers import DeviceSerializer, SurveySerializer, ErrorSerializer
# from .utils import DeviceManager, SensorManager
from .utils import create_client_key, generate_device, set_device_to_data, set_sensor_to_data
from ..models import Survey, Error

# class DeviceRestrictedCreateView(generics.GenericAPIView):
#     permission_classes = [DeviceRestrictionPermission]
#     # Request data getter
#     def get_request_data(self, request):
#         return request.data
#     # Create EXCEPTION data and status code
#     def get_exception_data(self, request):
#         return None
#     def get_exception_status(self, request):
#         return status.HTTP_400_BAD_REQUEST
#     # Serializer ERROR data and status code
#     def get_error_data(self, serializer):
#         return serializer.error
#     def get_error_status(self, serializer):
#         return status.HTTP_400_BAD_REQUEST
#     # Serializer SUCCESS data and status code
#     def get_success_data(self, serializer):
#         return serializer.data
#     def get_success_status(self, serializer):
#         return status.HTTP_201_CREATED
#     # create
#     def create(self, request, *args, **kwargs):
#         response_data = None
#         response_status = None
#         try:
#             data = self.get_request_data(request)
#             serializer = self.get_serializer(data=data, many=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 response_data = self.get_success_data(serializer)
#                 response_status = self.get_success_status(serializer)
#             else:
#                 response_data = self.get_error_data(serializer)
#                 response_status = self.get_error_status(serializer)
#         except:
#             response_data = self.get_exception_data(request)
#             response_status = self.get_exception_status(request)
#         return Response(response_data, response_status)

# class SurveyCreateView(DeviceRestrictedCreateView):
#     queryset = Survey.objects.all()
#     serializer_class = SurveySerializer

#     def get_request_data(self, request):
#         data = request.data    
#         data = DeviceManager.set_device_by_request(data, request)
#         data = SensorManager.set_sensor_by_enum(data)
#         return data

# class ErrorCreateView(DeviceRestrictedCreateView):
#     queryset = Error.objects.all()
#     serializer_class = ErrorSerializer

#     def get_request_data(self, request):
#         data = request.data    
#         data = DeviceManager.set_device_by_request(data, request)
#         return data



@api_view(['POST'])
@permission_classes([DeviceRegistrationPermission])
def device(request):
    mac_address = request.data['mac_address']
    data = generate_device(mac_address)
    serializer = DeviceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        ovpn_key = create_client_key(data)
        return Response(ovpn_key, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([DeviceRestrictionPermission])
def survey(request):
    data = request.data
    data = set_device_to_data(data, request)
    data = set_sensor_to_data(data)
    serializer = SurveySerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([DeviceRestrictionPermission])
def error(request):
    data = request.data
    data = set_device_to_data(data, request)
    serializer = ErrorSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
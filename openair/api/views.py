from ipware import get_client_ip
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import SurveyPermission
from .serializers import SurveySerializer
from .utils import get_and_update_request_data
from ..models import Survey

@api_view(['POST'])
@permission_classes([SurveyPermission])
def view(request):
    data = get_and_update_request_data(request)
    serializer = SurveySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# client_ip, is_routable = get_client_ip(request)
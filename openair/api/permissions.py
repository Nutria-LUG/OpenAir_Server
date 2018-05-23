from ipware import get_client_ip
from rest_framework import permissions
from .utils import get_device_or_none_by_request
from ..models import Device

class SurveyPermission(permissions.BasePermission):
    """
    Request IP belongs to registered and active device
    """

    def has_permission(self, request, view):
        ip_address = get_client_ip(request)
        device = get_device_or_none_by_request(request)
        if device:
            return device.active
        return False
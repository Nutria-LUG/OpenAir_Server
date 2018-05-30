from ipware import get_client_ip
from rest_framework import permissions
from .utils import get_device_by_request
from ..models import Device

class DevicePermission(permissions.BasePermission):
    """
    Request IP belongs to registered and active devices
    """

    def has_permission(self, request, view):
        device = get_device_by_request(request)
        if device:
            return device.active
        return False
from rest_framework import permissions
# from .utils import DeviceManager
from .utils import (
    get_first_free_device_enum,
    get_device_by_request,
    is_allowed_device_registration,
    get_max_devices_count
)

class DeviceRegistrationPermission(permissions.BasePermission):
    """
    Device registrations must be open
    and first free enum less or equal than max allowed count
    """

    def has_permission(self, request, view):
        if is_allowed_device_registration():
            enum = get_first_free_device_enum()
            if enum > 0 and enum <= get_max_devices_count():
                return True
        return False

class DeviceRestrictionPermission(permissions.BasePermission):
    """
    Request IP belongs to registered and active devices
    """

    def has_permission(self, request, view):
        device = get_device_by_request(request)
        return device.active if device else False
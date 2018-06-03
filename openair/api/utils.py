from django.conf import settings
from ipware import get_client_ip
from ..models import Device, Sensor

# class AbstractDeviceManager:
#     def get_device_by_request(self, request):
#         raise("abstract method")
#     def set_device_by_request(self, data, request):
#         raise("abstract method")

# class DeviceManager(AbstractDeviceManager):
#     request_manager = None

#     def __init__(self, request_manager):
#         self.request_manager = request_manager
    
#     def get_device_by_request(self, request):
#         client_ip = self.request_manager.get_client_ip(request)
#         return Device.objects.get(ip_address=client_ip)
#     def set_device_by_request(self, data, request):
#         device = self.get_device_by_request(request)
#         for item in data:
#             item.update({'device': device.pk})
#         return data

# class DeviceManagerProxy(AbstractDeviceManager):
#     device_manager = None

#     def __init__(self, device_manager):
#         self.device_manager = device_manager

#     def get_device_by_request(self, request):
#         try:
#             self.device_manager.get_device_by_request(request)
#         except Exception ex:
#             return None
#     def set_device_by_request(self, data, request):
#         try:
#             self.set_device_by_request(data, request)
#         except Exception ex:
#             return data

# class DeviceManagerFactory:
#     request_manager = None

#     def __init__(self, request_manager):
#         self.request_manager = request_manager
    
#     def create_debug(self):
#         return self.create_release()
#     def create_release(self):
#         device_manager = DeviceManager(self.request_manager)
#         return DeviceManagerProxy(device_manager)

# class SensorManager:
#     @staticmethod
#     def get_sensor_by_enum(enum):
#         try: return Sensor.objects.get(enum=enum)
#         except: return None
#     @staticmethod
#     def set_sensor_by_enum(data):
#         for item in data:
#             enum = item['sensor']
#             sensor = SensorManager.get_sensor_by_enum(enum)
#             item.update({'sensor': sensor.pk if sensor else None})
#         return data

# class RequestManager:
#     @staticmethod
#     def get_client_ip(request):
#         client_ip, is_routable = get_client_ip(request)
#         if not is_routable:
#             return client_ip
#         return None



# Device
def generate_device_name(enum):
    return 'Arietta%02d' % enum
def generate_device_mac_address(enum):
    return '10.0.8.1%02d' % enum
def generate_device(mac_address):
    enum = get_first_free_device_enum()
    return {
        'name': generate_device_name(enum),
        'mac_address': mac_address,
        'ip_address': generate_device_mac_address(enum),
        'enum': enum
    }
    # get first free enum value (eg. 1)
    # name = Arietta01
    # mac = mac_address
    # ip = 10.0.8.101
    # enum = 1
    # active = False
    # generate VPN key
    # return stringed VPN key
def get_device_by_request(request):
    client_ip, is_routable = get_client_ip(request)
    try: return Device.objects.get(ip_address=client_ip)
    except: return None
def get_first_free_device_enum():
    allowed_enums = range(1, 1 + get_max_devices_count())
    queryset = Device.objects.order_by('enum').values('enum')
    used_enums = [a['enum'] for a in queryset]
    free_enums = [a for a in allowed_enums if a not in used_enums]
    if len(free_enums) > 0:
        return free_enums[0]
    return -1
def set_device_to_data(data, request):
    device = get_device_by_request(request)
    if device:
        for item in data:
            item.update({'device': device.pk})
    return data

# OpenVPN
def create_client_key(device):
    return "abcdefghijklmnopqrstuvwxyz"

# Sensor
def set_sensor_to_data(data):
    for item in data:
        try:
            code = item['code']
            sensor = Sensor.objects.get(code=code)
            item.update({'sensor': sensor.pk})
        except: continue
    return data

# Settings
def is_allowed_device_registration():
    return settings.OA_DEVICE_REGISTRATION
def get_max_devices_count():
    return settings.OA_MAX_DEVICES_COUNT
from ipware import get_client_ip
from ..models import Device, Sensor

class DeviceUtils:
    pass

# Device
def get_device_by_request(request):
    client_ip, is_routable = get_client_ip(request)
    try: return Device.objects.get(ip_address=client_ip)
    except: return None
def set_device_by_request(request):
    data = request.data
    device = get_device_by_request(request)
    if device:
        data.update({'device': device.pk})
    return data

# Sensor
def get_sensor_by_request(request):
    code = request.data['sensor']
    try: return Sensor.objects.get(code=code)
    except: return None
def set_sensor_by_request(request):
    data = request.data
    sensor = get_sensor_by_request(request)
    if sensor:
        data.update({'sensor': sensor.pk})
    return data
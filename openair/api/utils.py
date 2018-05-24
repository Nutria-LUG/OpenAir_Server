from ipware import get_client_ip
from ..models import Device, Sensor

# Device
def get_device_or_none_by_ip(ip_address):
    try: return Device.objects.get(ip_address=ip_address)
    except: return None
def get_device_or_none_by_request(request):
    client_ip, is_routable = get_client_ip(request)
    return get_device_or_none_by_ip(client_ip)

# Sensor
def get_sensor_or_none_by_code(code):
    try: return Sensor.objects.get(code=code)
    except: return None

# Request
def get_and_update_request_data(request):
    data = request.data
    device = get_device_or_none_by_request(request)
    sensor = get_device_or_none_by_request(request)
    if device and sensor:
        data.update({'device': device.pk})
        data.update({'sensor': sensor.pk})
    return data
from ipware import get_client_ip
from ..models import Device, Sensor

def get_device_or_none_by_request(request):
    client_ip, is_routable = get_client_ip(request)
    return get_device_or_none_by_ip(client_ip)

def get_device_or_none_by_ip(ip_address):
    try:
        device = Device.objects.get(ip_address=ip_address)
        return device
    except:
        return None

def get_sensor_or_none_by_code(code):
    try:
        sensor = Sensor.objects.get(code=code)
        return sensor
    except:
        return None
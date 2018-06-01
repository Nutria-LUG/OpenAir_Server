from ipware import get_client_ip
from ..models import Device, Sensor

class DeviceUtils:
    pass

# Common
def get_request_data(request):
    data = request.data
    if not isinstance(data, list):
        return [data]
    return data

# Device
def get_device_by_request(request):
    client_ip, is_routable = get_client_ip(request)
    try: return Device.objects.get(ip_address=client_ip)
    except: return None
def set_device_to_data(data, request):
    device = get_device_by_request(request)
    if device:
        for item in data:
            item.update({'device': device.pk})
    return data

# Sensor
def set_sensor_to_data(data):
    for item in data:
        try:
            code = item['code']
            sensor = Sensor.objects.get(code=code)
            item.update({'sensor': sensor.pk})
        except: continue
    return data
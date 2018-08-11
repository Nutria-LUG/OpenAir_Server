from django.http import JsonResponse
from openair.models import *

LAST_NUMBER = 100

def get_last(request):
    surveys = Survey.objects.all().order_by("-timestamp")
    to_ret = []
    current = None
    last_timestamp = None
    counter = 0
    for survey in surveys:
        if counter == LAST_NUMBER:
            break
        if last_timestamp != survey.timestamp:
            counter = counter + 1
            last_timestamp = survey.timestamp
            counter = counter + 1
            current = {}
            to_ret.append(current)
        current[survey.sensor.enum] = {
            "value": survey.value,
            "timestamp": survey.timestamp
        }
    return JsonResponse({ "result": current });

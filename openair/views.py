from django.http import JsonResponse
from django.shortcuts import render
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
            current = {}
            to_ret.append(current)
        current[survey.sensor.enum] = {
            "value": survey.value,
            "timestamp": survey.timestamp
        }
    return JsonResponse({ "result": to_ret })

def get_all_datasets(request):
    data = request.GET
    sort = getattr(data, "sort") if hasattr(data, "sort") else "-timestamp"
    skip = getattr(data, "skip") if hasattr(data, "skip") else 0
    top = getattr(data, "top") if hasattr(data, "top") else 100
    surveys_queryset = Survey.objects.all().order_by(sort)[skip:top]
    surveys = []
    for survey in surveys_queryset:
        surveys.append({
            "sensor": survey.sensor.enum,
            "value": survey.value,
            "timestamp": survey.timestamp
        })
    return JsonResponse({"surveys": surveys})

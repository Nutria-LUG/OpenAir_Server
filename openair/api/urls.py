from django.urls import path
from .import views

urlpatterns = [
    path('device', views.device),
    path('survey', views.survey),
    path('error', views.error),
]

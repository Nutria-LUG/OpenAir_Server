from django.urls import path
from .import views

urlpatterns = [
    path('api/survey', views.survey),
    path('api/error', views.error),
]

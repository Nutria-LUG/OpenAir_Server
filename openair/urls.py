from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('openair.api.urls')),
    path('all-datasets', views.get_all_datasets),
]

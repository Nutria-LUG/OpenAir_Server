from django.urls import path, include

urlpatterns = [
    path('openair/', include('openair.api.urls')),
]

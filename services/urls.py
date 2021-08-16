from django.urls import path, include
from .views import services_views

urlpatterns = [
    path('', services_views),
]

from django.urls import path, include
from .views import *

urlpatterns = [
    path('sauna/', sauna_views),
    path('vat/', vat_views),
]

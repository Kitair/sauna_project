from django.urls import path, include
from .views import *

urlpatterns = [
    path('', contacts_views, name="contacts"),
]

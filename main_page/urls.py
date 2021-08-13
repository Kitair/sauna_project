from django.urls import path, include
from .views import main_views

urlpatterns = [
    path('', main_views),
]

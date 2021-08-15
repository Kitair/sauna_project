from django.shortcuts import render
from .models import *


def main_views(request):
    return render(request, 'services.html')
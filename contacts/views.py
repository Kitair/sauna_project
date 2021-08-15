from django.shortcuts import render
from .models import *


def contacts_views(request):
    return render(request, 'contacts.html')
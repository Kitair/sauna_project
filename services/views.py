from django.shortcuts import render
from .models import Services


def services_views(request):
    services = Services.objects.filter(is_visible=True)

    return render(request, 'services.html', context={'services': services, })

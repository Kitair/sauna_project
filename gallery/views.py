from django.shortcuts import render
from .models import Category, Gallery


def sauna_views(request):
    category = Category.objects.filter(is_visible=True).filter(is_sauna=True)
    gallery = Gallery.objects.filter(is_visible=True).filter(is_sauna=True)

    return render(request, 'gallery_sauna.html', context={'category': category, 'gallery': gallery,})


def vat_views(request):
    category = Category.objects.filter(is_visible=True).filter(is_vat=True)
    gallery = Gallery.objects.filter(is_visible=True).filter(is_vat=True)

    return render(request, 'gallery_vat.html', context={'category': category, 'gallery': gallery,})
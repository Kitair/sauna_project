from django.shortcuts import render
from .models import Slider, About, Offer, Events, Feedback


def main_views(request):
    slider = Slider.objects.filter(is_visible=True)
    about = About.objects.filter(is_visible=True)
    offer = Offer.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    feedback = Feedback.objects.filter(is_visible=True)

    return render(request, 'index.html', context={'slider': slider, 'about': about, 'offer': offer,
                                                  'events': events, 'feedback': feedback, })


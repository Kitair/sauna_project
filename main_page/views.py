from django.shortcuts import render, redirect
from .models import Slider, About, Offer, Events, Feedback
from .forms import FeedbackForm


def main_views(request):
    if request.method == 'POST':
        form_feedback = FeedbackForm(request.POST)

        if form_feedback.is_valid():
            form_feedback.save()
            return redirect('/')

    slider = Slider.objects.filter(is_visible=True)
    about = About.objects.filter(is_visible=True)
    offer = Offer.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    feedback = Feedback.objects.filter(is_visible=True)
    form_feedback = FeedbackForm()

    return render(request, 'index.html', context={'slider': slider, 'about': about, 'offer': offer,
                                                  'events': events, 'feedback': feedback,
                                                  'form_feedback': form_feedback, })

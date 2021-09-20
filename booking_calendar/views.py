from django.shortcuts import render, redirect
from django.views import View
from .models import Booking
from django.http import JsonResponse
from .forms import BookingForm


def bookingview(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    form_booking = BookingForm()

    return render(request, 'booking.html', context={'form_booking': form_booking})


class BookingView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        date = Booking.objects.all()
        return render(request, 'booking.html', {'date': date})


class CheckBookingDate(View):

    @staticmethod
    def get(request, *args, **kwargs):
        btnData = request.GET.get('btnData')
        btnService = request.GET.get('btnService')
        booked_service = list(Booking.objects.all().values_list('date_field', 'service_field', 'time_field'))
        booked_time = []
        for date, service, time in booked_service:
            if btnData in date and btnService in service:
                booked_time.append(time)
        if not booked_time:
            return JsonResponse({'data': False})
        else:
            return JsonResponse({'data': booked_time})


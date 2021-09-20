from django.urls import path
from .views import  CheckBookingDate, bookingview


urlpatterns = [
    path('', bookingview),
    path('check_booking_date/', CheckBookingDate.as_view(), name='check_booking_date')
]

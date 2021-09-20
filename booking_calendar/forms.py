from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    service_field = forms.CharField(max_length=5,
                                    widget=forms.TextInput(
                                        attrs={'name': 'service',
                                               'type': 'text',
                                               'readonly': 'readonly'}))

    data_field = forms.CharField(max_length=10,
                                 widget=forms.TextInput(
                                     attrs={'name': 'date',
                                            'type': 'text',
                                            'readonly': 'readonly'}))

    time_field = forms.CharField(max_length=5,
                                 widget=forms.TextInput(
                                     attrs={'name': 'time',
                                            'type': 'text',
                                            'readonly': 'readonly'}))

    user_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(
                                    attrs={'name': 'user_name',
                                           'type': 'text',
                                           'placeholder': "Иван Иванов"}))

    user_phone = forms.CharField(max_length=13,
                                 widget=forms.TextInput(
                                     attrs={'name': 'user_phone',
                                            'type': 'tel',
                                            'placeholder': "+38 (063) 000 00 00"}))

    class Meta:
        model = Booking
        fields = ('service_field', 'date_field', 'time_field', 'user_name', 'user_phone')

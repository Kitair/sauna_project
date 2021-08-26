from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    user_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(
                                    attrs={'class': 'feedback-input', 'name': 'user_name',
                                           'type': 'text',
                                           'placeholder': "Ваше имя", 'required': 'required'}))

    user_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'feedback-input', 'name': 'user_email',
               'type': 'email',
               'placeholder': "Ваша почта", 'required': 'required'}))

    user_message = forms.CharField(max_length=1000,
                                   widget=forms.Textarea(
                                       attrs={'class': 'feedback-textarea', 'name': 'user_message',
                                              'placeholder': "Ваш комментарий", 'required': 'required'}))

    class Meta:
        model = Feedback
        fields = ('user_name', 'user_email', 'user_message')

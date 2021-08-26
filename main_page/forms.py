from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    user_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(
                                    attrs={'class': 'feedback-input', 'name': 'username',
                                           'type': 'text',
                                           'placeholder': "Ваше имя", 'required': "required",
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    user_email = forms.EmailField(max_length=30,
                                  widget=forms.TextInput(
                                      attrs={'class': 'feedback-input', 'name': 'user-email',
                                             'type': 'email',
                                             'placeholder': "Ваша почта", 'required': "required",
                                             'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    user_message = forms.CharField(max_length=1000,
                                   widget=forms.TextInput(
                                       attrs={'class': 'feedback-textarea', 'name': 'user-feedback',
                                              'placeholder': "Ваш комментарий", 'required': "required",
                                              'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    class Meta:
        model = Feedback
        fields = ('user_name', 'user_email', 'user_message')

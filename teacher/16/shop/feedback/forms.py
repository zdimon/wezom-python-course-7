from django import forms
from django.forms import ModelForm
from .models import UserMessages

class FeedbackForm(ModelForm):
    class Meta:
        model = UserMessages
        fields = ['username', 'text']
from django.shortcuts import render
from .forms import FeedbackForm
from .models import UserMessages


def feed(request):
    form = FeedbackForm()
    if request.user.is_authenticated:
        userMessage = UserMessages()
        userMessage.username = request.user.username
        form = FeedbackForm(instance=userMessage)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
    return render(request,'feed.html',{"form": form})

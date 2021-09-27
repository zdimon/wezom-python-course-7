from django.contrib import admin
from django.urls import path
from main.views import index, check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('check/', check),
]

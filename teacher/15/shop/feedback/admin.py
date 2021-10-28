from django.contrib import admin
from .models import UserMessages
# Register your models here.
class UserMessagesAdmin(admin.ModelAdmin):
    list_display = ['username', 'text']

admin.site.register(UserMessages, UserMessagesAdmin)
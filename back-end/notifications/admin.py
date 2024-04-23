from django.contrib import admin
from .models import EmailNotification

@admin.register(EmailNotification)
class EmailNotificationAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'sent_at', 'status')
    list_filter = ('status', 'sent_at')
    search_fields = ('email', 'subject')

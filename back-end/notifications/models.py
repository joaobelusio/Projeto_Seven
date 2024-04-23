from django.db import models
from django.conf import settings

class EmailNotification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_notifications')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='sent', choices=(('sent', 'Sent'), ('failed', 'Failed')))

    def __str__(self):
        return f"Email to {self.email} - {self.subject} - Sent on {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

from django.db import models

class Message(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.text[:30]}... ({self.sentiment})"
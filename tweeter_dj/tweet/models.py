from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)  # Assuming a tweet can be up to 240 characters
    photo = models.ImageField(upload_to='tweets/', blank=True, null=True)  # Optional photo upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."  # Display first 20 characters of the tweet
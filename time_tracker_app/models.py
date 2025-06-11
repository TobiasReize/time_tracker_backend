from django.db import models
from django.contrib.auth.models import User

class Timestamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.CharField(max_length=30)
    end = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

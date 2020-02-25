from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Api(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apis')
from django.db import models

class ApiModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
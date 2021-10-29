from django.db import models

# Create your models here.
class ConnectModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()


from django.db import models

# Create your models here.
class ConnectModel(models.Model):
    myimage = models.ImageField()
    title = models.CharField(max_length=100)
    memo = models.TextField()
    def __str__(self):
        return self.title


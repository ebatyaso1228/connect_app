from django.db import models
from django.core.validators import validate_integer


# Create your models here.
class ConnectModel(models.Model):
    myimage = models.ImageField()
    title = models.CharField(max_length=100)
    memo = models.TextField()
    level = models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,)


    level_b = models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
    
  
    )




    def __str__(self):
        return self.title


from django.db import models
from django.core.validators import validate_integer


# Create your models here.
class ConnectModel(models.Model):
    myimage = models.ImageField(verbose_name='アイコン', upload_to='media')
    title = models.CharField(verbose_name='自分の名前', max_length=100)
    memo = models.TextField(verbose_name='開発経験')
    level = models.IntegerField(
        verbose_name='フロント力',
        blank=True,
        null=True,
        default=0,)


    level_b = models.IntegerField(
        verbose_name='バック力',
        blank=True,
        null=True,
        default=0,
    
  
    )




    def __str__(self):
        return self.title


# Generated by Django 3.2.8 on 2021-11-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectmodel',
            name='myimage',
            field=models.ImageField(default='/media/default.png', upload_to=''),
        ),
    ]

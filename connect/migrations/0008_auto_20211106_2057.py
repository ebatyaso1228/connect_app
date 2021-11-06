# Generated by Django 3.2.8 on 2021-11-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0007_connectmodel_level_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectmodel',
            name='level',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='フロント力'),
        ),
        migrations.AlterField(
            model_name='connectmodel',
            name='level_b',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='バック力'),
        ),
    ]

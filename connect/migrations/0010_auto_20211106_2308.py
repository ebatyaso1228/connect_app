# Generated by Django 3.2.8 on 2021-11-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0009_alter_connectmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectmodel',
            name='memo',
            field=models.TextField(verbose_name='開発経験'),
        ),
        migrations.AlterField(
            model_name='connectmodel',
            name='myimage',
            field=models.ImageField(upload_to='', verbose_name='アイコン'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201224_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=150),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=150),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=150),
        ),
    ]

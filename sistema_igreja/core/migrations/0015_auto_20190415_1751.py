# Generated by Django 2.1 on 2019-04-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190409_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipulo',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='lider',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

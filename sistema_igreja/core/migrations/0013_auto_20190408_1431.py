# Generated by Django 2.1 on 2019-04-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190408_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipulo',
            name='saiu',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Motivo*'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='saiu',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Motivo*'),
        ),
    ]

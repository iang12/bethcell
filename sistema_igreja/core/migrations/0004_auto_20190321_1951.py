# Generated by Django 2.1.5 on 2019-03-21 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_lider_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
                ('compra_sempre', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
                ('ctps', models.CharField(max_length=25)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='lider',
            options={},
        ),
        migrations.AlterField(
            model_name='lider',
            name='lider_de_rede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liderado', to='core.Lider', verbose_name='Lider*'),
        ),
    ]

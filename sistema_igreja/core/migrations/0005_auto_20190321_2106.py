# Generated by Django 2.1.5 on 2019-03-21 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190321_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=35, verbose_name='Nome do Grupo')),
                ('criado_em', models.DateField(verbose_name='Data de Abertura')),
                ('descricao', models.TextField(blank=True, verbose_name='Dia da Reunião')),
            ],
            options={
                'verbose_name_plural': 'Celulas',
                'verbose_name': 'Celula',
            },
        ),
        migrations.CreateModel(
            name='Discipulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, null=True, unique=True, verbose_name='Nome*')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo*')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento*')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tipo', models.CharField(blank=True, choices=[('N0', 'Novo Convertido'), ('N1', 'Cursando-N1'), ('N2', 'Cursando-N2'), ('N3', 'Cursando-N3'), ('N4', 'Cursando-Trainee'), ('N5', 'Trainee Formado'), ('LC', 'Lider de Célula'), ('LG', 'Lider de Geração'), ('PR', 'Pastores')], max_length=2, null=True, verbose_name='Tipo*')),
                ('celula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Celula')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lider',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='lider',
            name='nome',
            field=models.CharField(max_length=40, null=True, unique=True, verbose_name='Nome*'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo*'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='tipo',
            field=models.CharField(blank=True, choices=[('N0', 'Novo Convertido'), ('N1', 'Cursando-N1'), ('N2', 'Cursando-N2'), ('N3', 'Cursando-N3'), ('N4', 'Cursando-Trainee'), ('N5', 'Trainee Formado'), ('LC', 'Lider de Célula'), ('LG', 'Lider de Geração'), ('PR', 'Pastores')], max_length=2, null=True, verbose_name='Tipo*'),
        ),
        migrations.AddField(
            model_name='discipulo',
            name='lider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lider'),
        ),
        migrations.AddField(
            model_name='celula',
            name='lider',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Lider'),
        ),
    ]

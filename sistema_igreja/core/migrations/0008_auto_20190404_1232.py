# Generated by Django 2.1 on 2019-04-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190401_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celula',
            name='descricao',
        ),
        migrations.AddField(
            model_name='celula',
            name='celula_de',
            field=models.CharField(choices=[('H', 'Homens'), ('M', 'Mulheres'), ('J', 'Jovens')], default='J', max_length=1, verbose_name='Célula de'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celula',
            name='colider',
            field=models.CharField(default='J', max_length=35, verbose_name='Trainee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celula',
            name='dia_reuniao',
            field=models.TextField(choices=[('DM', 'Domingo'), ('SF', 'Segunda-feira '), ('TF', 'Terça-feira '), ('QF', 'Quarta-feira  '), ('QT', 'Quinta feira '), ('SF', 'sexta-feira'), ('SB', 'Sabado')], default='J', verbose_name='Dia da Reunião'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discipulo',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='discipulo',
            name='escolaridade',
            field=models.CharField(blank=True, choices=[('ANF', 'Não Alfabetizado'), ('EFI', 'Ensino fundamental incompleto'), ('EFC', 'Ensino fundamental completo'), ('EMI', 'Ensino médio incompleto'), ('EMC', 'Ensino médio completo'), ('ESC', 'Superior completo'), ('PGC', 'Pós-Graduação'), ('MES', 'Mestrado'), ('DOT', 'Doutorado')], max_length=3),
        ),
        migrations.AlterField(
            model_name='discipulo',
            name='uf',
            field=models.CharField(blank=True, choices=[('', 'Estado'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MT', 'Mato Grosso'), ('MA', 'Maranhão'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RS', 'Rio Grande do Sul'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='escolaridade',
            field=models.CharField(blank=True, choices=[('ANF', 'Não Alfabetizado'), ('EFI', 'Ensino fundamental incompleto'), ('EFC', 'Ensino fundamental completo'), ('EMI', 'Ensino médio incompleto'), ('EMC', 'Ensino médio completo'), ('ESC', 'Superior completo'), ('PGC', 'Pós-Graduação'), ('MES', 'Mestrado'), ('DOT', 'Doutorado')], max_length=3),
        ),
        migrations.AlterField(
            model_name='lider',
            name='uf',
            field=models.CharField(blank=True, choices=[('', 'Estado'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MT', 'Mato Grosso'), ('MA', 'Maranhão'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RS', 'Rio Grande do Sul'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF'),
        ),
    ]

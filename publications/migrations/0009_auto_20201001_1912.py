# Generated by Django 3.1.1 on 2020-10-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0008_auto_20201001_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('Fêmea', 'Fêmea'), ('Macho', 'Macho'), ('Sexo Desconhecido', 'Sexo Desconhecido')], default='Sexo Desconhecido', max_length=18, verbose_name='Sexo'),
        ),
    ]

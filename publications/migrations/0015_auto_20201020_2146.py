# Generated by Django 3.1.1 on 2020-10-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0014_auto_20201009_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='caracteristicas',
            field=models.TextField(max_length=200, verbose_name='Caracaterísticas'),
        ),
    ]

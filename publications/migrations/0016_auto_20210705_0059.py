# Generated by Django 3.1.1 on 2021-07-05 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0015_auto_20201020_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='categoria',
            field=models.CharField(choices=[('Perdido', 'Perdido'), ('Para Adoção', 'Para Adoção'), ('Encontrado', 'Encontrado'), ('Adotado', 'Adotado')], max_length=15, verbose_name='Categoria'),
        ),
    ]
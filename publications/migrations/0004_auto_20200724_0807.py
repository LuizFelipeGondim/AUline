# Generated by Django 3.0.8 on 2020-07-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20200724_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='like',
            field=models.IntegerField(blank=True),
        ),
    ]

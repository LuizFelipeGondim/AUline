# Generated by Django 3.1.1 on 2020-10-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20201009_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoacesso',
            old_name='numero_rua',
            new_name='numero_ponto',
        ),
        migrations.AlterField(
            model_name='depoimento',
            name='permissao',
            field=models.BooleanField(default=True, verbose_name='permissão'),
        ),
        migrations.AlterField(
            model_name='pontoacesso',
            name='desc_ponto',
            field=models.CharField(choices=[('Casa de apoiadores', 'Casa de apoiadores'), ('ONG sem fins lucrativos', 'ONG sem fins lucrativos')], max_length=40, verbose_name='Descrição do ponto'),
        ),
    ]
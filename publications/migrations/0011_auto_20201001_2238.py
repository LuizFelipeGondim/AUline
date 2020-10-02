# Generated by Django 3.1.1 on 2020-10-01 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_auto_20201001_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='motivo',
        ),
        migrations.CreateModel(
            name='MotivoDoacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField(max_length=600, verbose_name='Por que você está cadastrando esse animal?')),
                ('data_pub', models.DateField(auto_now=True, max_length=10, verbose_name='Data de nascimento')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.animal')),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-24 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Sem nome', max_length=50, verbose_name='Nome')),
                ('caracteristicas', models.TextField(blank=True, max_length=200, verbose_name='Caracaterísticas')),
                ('data_pub', models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')),
                ('imagem', models.ImageField(default='posts/unknown_animal.png', upload_to='posts', verbose_name='Imagem')),
                ('categoria', models.CharField(choices=[('P', 'Perdido'), ('PA', 'Para Adoção'), ('E', 'Encontrado'), ('A', 'Adotado')], max_length=15, verbose_name='Categoria')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'Fêmea'), ('M', 'Macho'), ('SE', 'Sexo Desconhecido')], max_length=8, verbose_name='Sexo')),
                ('porte', models.CharField(choices=[('PE', 'Pequeno'), ('ME', 'Médio'), ('GR', 'Grande')], max_length=8, verbose_name='Porte')),
                ('vacinado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=20, verbose_name='Vacinado')),
                ('vermifugado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=20, verbose_name='Vermifugado')),
                ('castrado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=20, verbose_name='Castrado')),
                ('tipo_animal', models.CharField(choices=[('CA', 'Cachorro'), ('GA', 'Gato')], max_length=20, verbose_name='Tipo do animal')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('rua', models.CharField(max_length=70, verbose_name='Rua')),
                ('raca', models.CharField(default='Não informada', max_length=70, verbose_name='Raça')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-data_pub',),
            },
        ),
    ]

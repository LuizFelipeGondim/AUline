from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Animal(models.Model):

    ESTADOS = (
        ('P', 'Perdido'),
        ('PA', 'Para Adoção'),
        ('E', 'Encontrado'),
        ('A', 'Adotado'),
    )

    SEXO = (
        ('Fêmea', 'Fêmea'),
        ('Macho', 'Macho'),
        ('Sexo Desconhecido', 'Sexo Desconhecido')
    )

    PORTE = (
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    )

    ESCOLHAS = (
        ('S', 'Sim'),
        ('N', 'Não'),
        ('NI', 'Não Informado'),
    )

    TIPO_ANIMAL = (
        ('CA', 'Cachorro'),
        ('GA', 'Gato'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    nome = models.CharField('Nome', max_length=50, default='Sem nome')
    caracteristicas = models.TextField('Caracaterísticas', max_length=200, blank=True)

    data_pub = models.DateTimeField('Data de Publicação', auto_now=True)

    imagem = models.ImageField('Imagem', upload_to='posts', default='posts/unknown_animal.png')
    categoria = models.CharField('Categoria', max_length=15, choices=ESTADOS)

    sexo = models.CharField('Sexo', max_length=18, choices=SEXO, default='Sexo Desconhecido')
    porte = models.CharField('Porte', max_length=8, choices=PORTE)

    vacinado = models.CharField('Vacinado', choices=ESCOLHAS, max_length=20, default='NI')
    vermifugado = models.CharField('Vermifugado', choices=ESCOLHAS, max_length=20, default='NI')
    castrado = models.CharField('Castrado', choices=ESCOLHAS, max_length=20, default='NI')

    tipo_animal = models.CharField('Tipo do animal', choices=TIPO_ANIMAL, max_length=20)

    idade = models.CharField('Idade', max_length=40)

    estado = models.CharField('Estado', max_length=50, blank=False)
    cidade = models.CharField('Cidade', max_length=50, blank=False)
    rua = models.CharField('Rua', max_length=70, blank=False)

    raca = models.CharField('Raça', max_length=70, default='Não informada')

    motivo = models.TextField('Por que você está cadastrando esse animal?', max_length=400)


    class Meta:
        ordering = ('-data_pub', )

    def __str__(self):
        return self.nome



from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    nome = models.CharField('Nome(Opcional)', max_length=80, default='Anônimo')
    data_envio = models.DateTimeField('Comentado em', auto_now=True)
    conteudo = models.TextField('Como podemos ajudá-lo?', max_length=300)
    email = models.EmailField('E-mail', max_length=100)
    titulo = models.CharField('Título', max_length=80)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-data_envio',)


class Depoimento(models.Model):
    cadastrante = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_coment = models.DateTimeField(auto_now=True)
    autor = models.CharField('Autor', max_length=80)
    conteudo = models.TextField('Depoimento', max_length=400)
    permissao = models.BooleanField('permissão', default=True)


    def __str__(self):
        return self.autor



class PontoAcesso(models.Model):

    TIPO_PONTO = (
        ('PA', 'Ponto para Adoção'),
        ('PD', 'Ponto para Doação'),
        ('PDA', 'Ponto para Doação e Adoção'),
    )

    DESC_PONTO = {
        ('ONG sem fins lucrativos', 'ONG sem fins lucrativos'),
        ('Casa de apoiadores', 'Casa de apoiadores'),
    }

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estado_ponto = models.CharField('Estado', max_length=50, blank=False)
    cidade_ponto = models.CharField('Cidade', max_length=50, blank=False)
    rua_ponto = models.CharField('Rua', max_length=70, blank=False)
    numero_rua = models.CharField('Número do ponto', max_length=70, blank=False)
    referencia = models.CharField('Referência', max_length=70, blank=False)
    nome_ponto = models.CharField('Nome do ponto', max_length=70, blank=False)
    telefone = models.CharField('Telefone Fixo', max_length=15)
    whatsapp = models.CharField('Whatsapp', max_length=15)
    tipo_ponto = models.CharField('Tipo do ponto', choices=TIPO_PONTO, max_length=20)
    desc_ponto = models.CharField('Descrição do ponto', choices=DESC_PONTO, max_length=40)
    imagem = models.ImageField('Imagem', upload_to='points', blank=False)

    def __str__(self):
        return self.nome_ponto 

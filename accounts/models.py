from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Foto de Perfil', upload_to='perfil', default='perfil/unknow.png')
    data_de_nascimento = models.DateField('Data de nascimento', max_length=10)
    whatsapp = models.CharField('Whatsapp', max_length=15)
    estado_usuario = models.CharField('Estado', max_length=50)
    cidade_usuario = models.CharField('Cidade', max_length=50, blank=True)
    biografia = models.TextField('Fale um pouco sobre você', max_length=400, blank=True)

    def __str__(self):
        return self.usuario.username

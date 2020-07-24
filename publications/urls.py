from .views import lista_animal, cadastro_animal, perfil_animal, contato
from django.urls import path

urlpatterns = [
    path('', lista_animal),
    path('cadastro-animal', cadastro_animal, name='cadastro-animal'),
    path('perfil-animal/<int:id>/', perfil_animal, name='perfil-animal'),
    path('entre-em-contato', contato, name='entre-em-contato'),
]
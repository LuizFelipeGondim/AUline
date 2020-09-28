from . import views
from django.urls import path

urlpatterns = [
    path('', views.lista_animal),
    path('cadastro-animal', views.cadastro_animal, name='cadastro-animal'),
    path('perfil-animal/<int:id>/', views.perfil_animal, name='perfil-animal'),
    path('entre-em-contato', views.contato, name='entre-em-contato'),
]
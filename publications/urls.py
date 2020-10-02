from . import views
from django.urls import path

urlpatterns = [
    path('', views.lista_animal),
    path('cadastro-animal', views.cadastro_animal, name='cadastro-animal'),
    path('cadastro-animal/motivo/<int:id>/', views.cadastro_motivo, name='cadastro-motivo'),
    path('perfil-animal/<int:id>/', views.perfil_animal, name='perfil-animal'),
    path('entre-em-contato/', views.contato, name='entre-em-contato'),
    path('doe/', views.doe, name='doe'),
    path('incentivo/', views.incentivo, name='incentivo'),
    path('sobre-nos', views.sobre, name='sobre'),
]
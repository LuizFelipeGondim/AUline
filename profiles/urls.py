from . import views
from django.urls import path

urlpatterns = [
    path('', views.perfil, name='perfil-usuario'),
    path('alterar-informacoes/<int:id>/', views.alterar_informacoes, name='alterar-informacoes'),
    path('excluir-animal/<int:id_animal>/', views.excluir_animal, name='excluir-animal'),
    path('editar-animal/<int:id_animal>/', views.editar_animal, name='editar-animal'),
    path('animal/<int:id>/', views.perfil_animal, name='perfil-animal'),
    path('excluir-conta/', views.excluir_conta, name='excluir-conta'),
]
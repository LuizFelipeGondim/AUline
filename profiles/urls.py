from . import views
from django.urls import path

urlpatterns = [
    path('animais', views.perfil, name='animais'),
    path('alterar-informacoes/<int:id>/', views.alterar, name='alterar-informacoes'),
    path('informacoes-pessoais', views.informacoes, name='informacoes-pessoais'),
    path('excluir-animal/<int:id_animal>/', views.excluir_animal, name='excluir-animal'),
    path('editar-animal/<int:id_animal>/', views.editar_animal, name='editar-animal'),
]
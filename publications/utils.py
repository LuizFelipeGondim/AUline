from .models import Animal
from django.db.models import Q


def animal_filter(request, lista_de_animais):
    lista_de_animais = Animal.objects.filter(
            Q(nome__icontains=request.POST.get('nome')),
            Q(cidade__icontains=request.POST.get('cidade')),
            
        )

    if request.POST.get('categoria_filtro'):
        lista_de_animais = lista_de_animais.filter(categoria=request.POST.get('categoria_filtro'))

    if request.POST.get('sexo'):
        lista_de_animais = lista_de_animais.filter(sexo=request.POST.get('sexo'))

    if request.POST.get('porte'):
        lista_de_animais = lista_de_animais.filter(porte=request.POST.get('porte'))

    if request.POST.get('tipo'):
        lista_de_animais = lista_de_animais.filter(tipo_animal=request.POST.get('tipo'))


    return lista_de_animais

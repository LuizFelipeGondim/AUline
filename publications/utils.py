from .models import Animal
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def filtro_animal(request, lista_de_animais):
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


def paginacao(request, lista_de_animais):
     #Paginação
    page = request.GET.get('page', 1)

    paginator = Paginator(lista_de_animais, 24)
    try:
        animais = paginator.page(page)
    except PageNotAnInteger:
        animais = paginator.page(1)
    except EmptyPage:
        animais = paginator.page(paginator.num_pages)

    return animais
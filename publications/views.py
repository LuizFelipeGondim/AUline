from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.models import Perfil
from django.core.paginator import Paginator
from services.forms import ContatoForm


def lista_animal(request):
    categorias = {}
    ids = []
    nome = ''
    categoria_filtro = ''
    sexo = ''
    porte = ''
    cidade = ''
    
    lista_de_animais = Animal.objects.all()

    #filtro de animais
    if request.method == 'POST':
        if request.POST.get('nome'):
            nome = request.POST.get('nome')
            lista_de_animais = lista_de_animais.filter(nome=nome)

        if request.POST.get('categoria_filtro'):
            categoria_filtro = request.POST.get('categoria_filtro')
            lista_de_animais = lista_de_animais.filter(categoria=categoria_filtro)

        if request.POST.get('sexo'):
            sexo = request.POST.get('sexo')
            lista_de_animais = lista_de_animais.filter(sexo=sexo)

        if request.POST.get('cidade'):
            cidade = request.POST.get('cidade')
            lista_de_animais = lista_de_animais.filter(cidade=cidade)

        if request.POST.get('porte'):
            porte = request.POST.get('porte')
            lista_de_animais = lista_de_animais.filter(porte=porte)
    
    #paginação das publicações
    paginator = Paginator(lista_de_animais, 15)
    page = request.GET.get('page')
    animais = paginator.get_page(page)
    
    #transformando as categorias em dicionário para trabalhar com javascript
    for animal in animais:
        categorias[animal.id] = animal.categoria
        ids.append(animal.id)

    contexto = {
        'nome':nome,
        'categoria_filtro':categoria_filtro,
        'cidade':cidade, 
        'sexo':sexo,
        'porte':porte,
        'animais': animais,
        'categorias': categorias,
        'ids': ids,
    }
    return render(request, 'index.html', contexto)


@login_required
def cadastro_animal(request):

    form = AnimalForm(request.POST or None, request.FILES)
    id_user = request.user.id

    if request.method == 'POST' and form.is_valid():
        user = User.objects.get(id=request.user.id)
        animal = form.save(commit=False)
        animal.usuario = user
        animal.save()
        return redirect('/')

    return render(request, 'cadastro-animal.html', {'form':form})

@login_required
def perfil_animal(request, id):
    animal = Animal.objects.get(id=id)

    endereco = animal.rua + ' ' + animal.cidade + ' ' + animal.estado
    contexto = {
        'animal':animal,
        'endereco': endereco,
    }
   
    return render(request, 'perfil-animal.html', contexto) 

def contato(request):
    form = ContatoForm(request.POST or None)

    contexto = {
        'form':form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'entre-em-contato.html', contexto)
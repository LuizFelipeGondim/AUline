from django.shortcuts import render, redirect
from .models import Animal
from services.models import PontoAcesso, Depoimento
from .forms import AnimalForm, MotivoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.models import Perfil
from services.forms import ContatoForm
from .utils import filtro_animal, paginacao
import requests

def lista_animal(request):
    categorias = {}
    ids = []
    lista_de_animais = Animal.objects.all()

    if request.method == 'POST':
       lista_de_animais = filtro_animal(request, lista_de_animais)

    animais = paginacao(request, lista_de_animais)
    
    #transformando as categorias em dicionário para trabalhar com javascript
    for animal in lista_de_animais:
        categorias[animal.id] = animal.categoria
        ids.append(animal.id)

    contexto = {
        'animais': animais,
        'categorias': categorias,
        'ids': ids,
    }
    return render(request, 'index.html', contexto)


@login_required
def cadastro_animal(request):

    form = AnimalForm(request.POST or None, request.FILES)

    '''def get_estados():
        lista_estados = []
        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        estados_json = response.json()
        for estado in estados_json:
            for key, value in estado.items():
                if key == 'sigla':
                    sigla = value

                if key == 'nome':
                    nome = value
            lista_estados.append(dict([('sigla', sigla), ('nome', nome)]))

        print(lista_estados)           
        return 0

    get_estados()'''
    if request.method == 'POST' and form.is_valid():
        user = User.objects.get(id=request.user.id)
        animal = form.save(commit=False)
        animal.usuario = user
        animal.save()
        return redirect('cadastro-motivo', animal.id)

    return render(request, 'cadastro-animal.html', {'form':form})

@login_required
def cadastro_motivo(request, id):
    form = MotivoForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        animal = Animal.objects.get(id=id)
        motivo = form.save(commit=False)
        motivo.animal_id = animal
        motivo.save()
        return redirect('/')

    return render(request, 'motivo.html', {'form':form}) 

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


def doe(request):
    pontos = PontoAcesso.objects.exclude(tipo_ponto='PA')
    
    contexto = {
        'pontos':pontos
    }

    return render(request, 'doe.html', contexto)

def incentivo(request):
    pontos = PontoAcesso.objects.exclude(tipo_ponto='PD')
    depoimentos = Depoimento.objects.all()

    contexto = {
        'pontos':pontos,
        'depoimentos': depoimentos,
    }

    return render(request, 'incentivo.html', contexto)
    
def sobre(request):
    return render(request, 'sobre.html')

def handler404(request, exception):
    return render(request, 'erro.html')

def handler500(request):
    return render(request, 'erro.html')
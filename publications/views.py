from django.shortcuts import render, redirect
from .models import Animal, MotivoCadastro
from services.models import PontoAcesso, Depoimento
from .forms import AnimalForm, MotivoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.models import Perfil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from services.forms import ContatoForm
from .utils import animal_filter

def lista_animal(request):
    categorias = {}
    ids = []
    lista_de_animais = Animal.objects.all()

    if request.method == 'POST':
       lista_de_animais = animal_filter(request, lista_de_animais)

    #Paginação
    page = request.GET.get('page', 1)

    paginator = Paginator(lista_de_animais, 24)
    try:
        animais = paginator.page(page)
    except PageNotAnInteger:
        animais = paginator.page(1)
    except EmptyPage:
        animais = paginator.page(paginator.num_pages)
    
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

@login_required
def perfil_animal(request, id):
    animal = Animal.objects.get(id=id)
    motivo = MotivoCadastro.objects.get(animal_id=id)
    responsavel = User.objects.get(id=animal.usuario.id)
    perfil_responsavel = Perfil.objects.get(usuario=responsavel.id)
    endereco = animal.rua + ' ' + animal.cidade + ' ' + animal.estado
    
    contexto = {
        'motivo':motivo,
        'animal':animal,
        'endereco': endereco,
        'responsavel': responsavel,
        'perfil_responsavel': perfil_responsavel
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
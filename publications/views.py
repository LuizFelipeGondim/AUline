from django.shortcuts import render, redirect
from .models import Animal, MotivoCadastro
from .forms import AnimalForm, MotivoForm
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

        if request.POST.get('tipo'):
            tipo = request.POST.get('tipo')
            lista_de_animais = lista_de_animais.filter(tipo_animal=tipo)
    
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

    endereco = animal.rua + ' ' + animal.cidade + ' ' + animal.estado
    
    contexto = {
        'motivo':motivo,
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

def doe(request):
    return render(request, 'doe.html')

def incentivo(request):
    return render(request, 'incentivo.html')
    
def sobre(request):
    return render(request, 'sobre.html')
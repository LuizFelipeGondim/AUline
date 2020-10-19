from django.shortcuts import render, redirect
from publications.models import Animal, MotivoCadastro
from django.contrib.auth.models import User
from accounts.models import Perfil
from accounts.forms import UserForm, PerfilForm
from publications.forms import AnimalForm, MotivoForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
import os

@login_required
def perfil(request):
    categorias = {}
    ids = []
    animais = Animal.objects.filter(usuario=request.user.id)
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(usuario=request.user.id).first

    for animal in animais:
        categorias[animal.id] = animal.categoria
        ids.append(animal.id)
    
    contexto = {
        'animais':animais,
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
        'ids':ids,
        'categorias':categorias,
    }
    
    return render(request, 'perfil.html', contexto)

@login_required
def alterar(request, id):
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(usuario=request.user.id)
    form_perfil = PerfilForm(request.POST or None, request.FILES or None, 
                            instance=perfil_usuario)
                            
    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
        'form_perfil':form_perfil,
    }

    if request.method == 'POST':
        if form_perfil.is_valid():
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            form_perfil.save()
            return redirect('perfil-usuario')
        
    return render(request,'alterar-informacoes.html', contexto)

@login_required
def editar_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    motivo = MotivoCadastro.objects.get(animal_id=id_animal)
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(usuario=request.user.id)

    form_motivo = MotivoForm(request.POST or None, instance=motivo)
    form = AnimalForm(request.POST or None, request.FILES or None,
                    instance=animal)

        
    if request.method == 'POST':
        if form.is_valid() and form_motivo.is_valid():
            form_motivo.save()
            form.save()
            return redirect('perfil-usuario')

    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
        'form':form,
        'form_motivo':form_motivo,
        'animal':animal,
    }

    return render(request, 'editar-animal.html', contexto)

@login_required
def excluir_conta(request):

    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        usuario.delete()
        logout(request)
        return redirect('/')

    return render(request, 'excluir-conta.html')

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

@login_required
def excluir_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    animal.delete()
    return redirect('perfil-usuario')


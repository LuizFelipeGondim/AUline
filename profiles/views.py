from django.shortcuts import render, redirect
from publicacoes.models import Animal
from django.contrib.auth.models import User
from users.models import Perfil
from users.forms import UserForm, PerfilForm
from publicacoes.forms import AnimalForm
from django.contrib.auth.decorators import login_required 

@login_required
def perfil(request):
    categorias = {}
    ids = []
    animais = Animal.objects.filter(usuario=request.user.id)
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(user=request.user.id).first

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
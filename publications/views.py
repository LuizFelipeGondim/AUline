from django.shortcuts import render, redirect
from .models import Animal, Comentario
from .forms import AnimalForm, ComentarioForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.models import Perfil
from django.core.paginator import Paginator


def lista_animal(request):
    
    return render(request, 'index.html')

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

def perfil_animal(request):
    return render(request, 'perfil-animal.html')
from django.shortcuts import render, redirect
from .forms import UserForm, PerfilForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserForm(request.POST)
        form_perfil = PerfilForm(request.POST)

        if form.is_valid() and form_perfil.is_valid():
            user = form.save()
            
            perfil = form_perfil.save(commit=False)
            perfil.usuario = user

            perfil.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            auth_login(request, user)
            return redirect('/')
    else:
        form = UserForm()
        form_perfil = PerfilForm()

    contexto = {
        'form':form,
        'form_perfil':form_perfil,
    }

    return render(request, 'cadastro.html', contexto)


def login(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credenciais inválidas')
            return redirect('login')
    
    else:
        return render(request, 'login.html')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



from django.forms import ModelForm
from .models import Contato
from django import forms 

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = {'nome', 'email', 'conteudo', 'titulo'}
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-input'}),
            'titulo': forms.TextInput(attrs={'class':'form-input'}),
            'conteudo': forms.Textarea(attrs={'class':'form-textarea', "rows":5, "cols":20}),
            'email': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Informe seu melhor e-mail'}),
        }
        
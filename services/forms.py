from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'conteudo', 'titulo']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-input'}),
            'titulo': forms.TextInput(attrs={'class':'form-input'}),
            'conteudo': forms.Textarea(attrs={'class':'form-textarea', "rows":5, "cols":20}),
            'email': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Informe seu melhor e-mail'}),
        }
        
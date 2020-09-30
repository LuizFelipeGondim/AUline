from django.forms import ModelForm
from .models import Animal
from django import forms

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'caracteristicas', 'imagem', 'sexo', 'vacinado', 'vermifugado',
        'categoria', 'castrado', 'cidade', 'rua', 'porte', 'estado', 'tipo_animal', 'raca', 
        'motivo']

        widgets = {
            'categoria': forms.Select(attrs={'class':'form-input'}),
            'tipo_animal': forms.Select(attrs={'class':'form-input'}),
            'porte': forms.Select(attrs={'class':'form-input'}),
            'sexo': forms.Select(attrs={'class':'form-input'}),
            'vacinado': forms.Select(attrs={'class':'form-input'}),
            'vermifugado': forms.Select(attrs={'class':'form-input'}),
            'castrado': forms.Select(attrs={'class':'form-input'}),
            'nome': forms.TextInput(attrs={'class':'form-input'}),
            'caracteristicas': forms.Textarea(attrs={'rows':5, 'cols':40, 'class':'form-textarea'} ),
            'cidade': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Cidade atual do animal'}),
            'rua': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Rua onde foi visto pela última vez'}),
            'estado': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Estado atual do animal'}),
            'raca': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Informe a raça'}),
            'motivo': forms.Textarea(attrs={'class':'form-input', 'placeholder':'Informe o motivo'}),
            'imagem': forms.FileInput(attrs={'class':'form-input'}),
            
        }

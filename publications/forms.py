from django import forms
from .models import Animal, MotivoCadastro
from django import forms

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'caracteristicas', 'imagem', 'sexo', 'vacinado', 'vermifugado',
        'categoria', 'castrado', 'cidade', 'rua', 'porte', 'estado', 'tipo_animal', 'raca', 'idade']

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
            'idade': forms.TextInput(attrs={'class':'form-input', 'placeholder':'1 ano e 2 meses'}),
            'rua': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Rua onde foi visto pela última vez'}),
            'estado': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Estado atual do animal'}),
            'raca': forms.TextInput(attrs={'class':'form-input', 'placeholder':'Informe a raça'}),
            'imagem': forms.FileInput(attrs={'class':'form-input'}),
            
        }

class MotivoForm(forms.ModelForm):
    class Meta:
        model = MotivoCadastro
        fields = ['motivo']

        widgets = {
           
            'motivo': forms.Textarea(attrs={'rows':5, 'cols':40, 'class':'form-textarea'} ),    
            
        }
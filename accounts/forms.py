from django import forms 
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'********'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-input'}),
            'email': forms.EmailInput(attrs={'class':'form-input'}),
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
        }

    '''def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user'''

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('data_de_nascimento', 'whatsapp', 'avatar', 'cidade_usuario', 'estado_usuario', 'biografia')
        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={'class':'form-input', 'placeholder':'DD/MM/YYYY'}),
            'whatsapp': forms.TextInput(attrs={'class':'form-input', 'placeholder':'(77)98888-8888'}),
            'cidade_usuario': forms.TextInput(attrs={'class':'form-input', }),
            'estado_usuario': forms.TextInput(attrs={'class':'form-input'}),
            'biografia': forms.Textarea(attrs={'rows':8, 'cols':40, 'class':'form-textarea'}),
        }
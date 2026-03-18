from django import forms
from .models import Cliente, GeneroJuego, Plataforma, Juego,Boleta
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'correo']
        labels = {
            'nombre_cliente': 'Nombre del Cliente',
            'correo': 'Correo Electrónico',
        }
        widgets = { 
                'nombre_cliente':forms.TextInput(attrs={'class': 'form-control', 'required': True}),
                'correo':forms.EmailInput(attrs={'class': 'form-control', 'required': True}), }
        

class GeneroJuegoForm(forms.ModelForm):
    class Meta:
        model = GeneroJuego
        fields = ['nombre_genero']
        labels = {
            'nombre_genero': 'Nombre del Género',
        }
        widgets = { 
                'nombre_genero':forms.TextInput(attrs={'class': 'form-control', 'required': True}), }
        
        
class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nombre_plataforma']
        labels = {
            'nombre_plataforma': 'Plataforma'
        }
        widgets = {
            'nombre_plataforma': forms.TextInput(attrs={'class': 'form-control', 'required': True})
        }
        

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre_juego', 'descripcion', 'imagen', 'genero', 'plataforma', 'precio']
        labels = {
            'nombre_juego': 'Nombre del Juego',
            'descripcion': 'Descripción',
            'imagen': 'Imagen del Juego',
            'genero': 'Género del Juego',
            'plataforma': 'Plataforma del Juego',
            'precio': 'Precio del Juego',
        }
        widgets = {
            'nombre_juego': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'plataforma': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'step': 0.01}),
        }
        
        
class CarritoClienteForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['cliente']
        labels = {
            'cliente': 'Cliente',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }
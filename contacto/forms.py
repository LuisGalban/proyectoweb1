from django import forms

class Contacto(forms.Form):
    
    nombre = forms.CharField(label='nombre', max_length=50, required=True)
    email = forms.EmailField(label='email', required=True)
    contenido = forms.CharField(label='contenido', widget=forms.Textarea, required=True)
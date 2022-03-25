# Imports

from django.shortcuts import render, redirect
from .forms import Contacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    FormContacto = Contacto()

    if request.method =="POST":
        FormContacto = Contacto(data=request.POST)

        if FormContacto.is_valid():
            nombre = request.POST.get("nombre")
            email  = request.POST.get("email")
            contenido = request.POST.get("contenido")

            sent = EmailMessage("Contacto pagina",
            "Usuario: {} \n Correo: {} \n Mensaje: {}".format(nombre,email,contenido),
            "michael342tv@hotmail.com",reply_to = [email])

            try:
                sent.send()
                return redirect("/contacto/?ok")

            except:
                return redirect("/contacto/?bad")

    return render(request, "contacto/contacto.html",{'Formulario_Contacto':FormContacto})
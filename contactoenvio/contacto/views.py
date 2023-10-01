from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import MiFormulario 
# Create your views here.

def contact(request):
    return render(request, "contacto.html")

# def contactar(request):
    
#     if request.method=="POST":
#         subject=request.POST["asunto"]
#         message=request.POST["mensaje"] + " " + request.POST["correo"]
#         email_from=settings.EMAIL_HOST_USER
#         recipient_list=["jahirfloresreyes20@gmail.com"]
#         send_mail(subject, message, email_from, recipient_list)
#         return render(request, "contacto.html")
#     return render(request, "contacto.html")

# def contactar(request):
     
#       if request.method == "POST":
#           subject = request.POST["asunto"]
#           message = request.POST["mensaje"] + " " + request.POST["correo"]
#           email_from = settings.EMAIL_HOST_USER
#           recipient_list = ["jahirfloresreyes20@gmail.com"]
       
#           try:
#               send_mail(subject, message, email_from, recipient_list)
#               # Agrega un mensaje de éxito
#               messages.success(request, 'El correo se ha enviado exitosamente.')
#           except Exception as e:
#               # En caso de error, puedes agregar un mensaje de error
#               messages.error(request, 'Ha ocurrido un error al enviar el correo: {}'.format(str(e)))

#       return render(request, "contacto.html")



def contactar(request):
    if request.method == "POST":
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            subject = formulario.cleaned_data['asunto']
            message = formulario.cleaned_data['mensaje'] + " " + formulario.cleaned_data['correo']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["jahirfloresreyes20@gmail.com"]
            
            try:
                send_mail(subject, message, email_from, recipient_list)
                # Agregar un mensaje de éxito
                messages.success(request, 'El correo se ha enviado exitosamente.')
            except Exception as e:
                # En caso de error, agregar un mensaje de error
                messages.error(request, 'Ha ocurrido un error al enviar el correo: {}'.format(str(e)))
    else:
        formulario = MiFormulario()  # Crea una instancia del formulario en caso de una solicitud GET

    return render(request, "contacto.html", {'formulario': formulario})




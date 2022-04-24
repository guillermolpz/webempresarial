import imp
from unicodedata import name
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm
    
    #Resivir valores del formulario
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            content = request.POST.get('content', '')
            
            # Creamos el correo
            mail = EmailMessage(
                "La Sabrosa: Nuevo mensaje de contacto", #Asunto
                "De {} {}\n\nEscribió:\n\n{}".format(name, mail, content), #Mensaje
                "lasabrosa.com", #Email de Origen
                ["correo_prueba@email.com"], #Email de destino
                reply_to=[mail]
            )
            
            # Lo enviamos y redireccionamos
            try:
                mail.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha salido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            
    return render(request, 'contact.html', {'form': contact_form})

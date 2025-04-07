from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('servicios')
            except:
                return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Usuario ya existe'
                        })
        return  render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coiciden'
                })
    
def servicios(request):
    if not request.user.is_authenticated:
        return  render(request, 'IniciarSesion.html', {
            'form': AuthenticationForm,
            'error': 'Nesesitas Iniciar Sesión'
        }) 
    else:
        return render(request, 'servicios.html')

def signout(request):
    logout(request)
    return redirect('home')

def IniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'IniciarSesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'IniciarSesion.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('servicios')

def despliegueServidores(request):
    if not request.user.is_authenticated:
        return  render(request, 'IniciarSesion.html', {
            'form': AuthenticationForm,
            'error': 'Nesesitas Iniciar Sesión'
        }) 
    else:
        return render(request, 'despliegueServidores.html')

def implementacionIa(request):
    if not request.user.is_authenticated:
        return  render(request, 'IniciarSesion.html', {
            'form': AuthenticationForm,
            'error': 'Nesesitas Iniciar Sesión'
        }) 
    else:
        return render(request, 'implementacionIa.html')

def servicioWeb(request):
    if not request.user.is_authenticated:
        return  render(request, 'IniciarSesion.html', {
            'form': AuthenticationForm,
            'error': 'Nesesitas Iniciar Sesión'
        }) 
    else:
        return render(request, 'servicioWeb.html')
    
# views.py
from django.contrib.auth.decorators import login_required
from .forms import SolicitudServicioForm

# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import SolicitudServicioForm

def solicitar_servicio(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            # Asocia la solicitud al usuario logueado
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user  # Asocia el usuario logueado
            solicitud.save()

            # Datos del correo
            subject = 'Nueva solicitud de servicio'
            message = f'Una nueva solicitud de servicio ha sido recibida:\n\nNombre: {solicitud.nombre}\nServicio: {solicitud.servicio.nombre}\nMensaje: {solicitud.mensaje}\nTelefono: {solicitud.telefono}\nEmail: {solicitud.email}\nDirección: {solicitud.direccion}'
            from_email = settings.DEFAULT_FROM_EMAIL  # Se toma de los settings (puedes configurarlo en settings.py)
            recipient_list = ['destinatario@correo.com']  # Este es el destinatario

            # Enviar el correo
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'servicios.html', {
                'mensaje':'Tu solicitud ha sido enviada con éxito. Nos pondremos en contacto contigo tan pronto como estemos disponibles. ¡Gracias!'
            })  # Redirige a una página de confirmación
    else:
        form = SolicitudServicioForm()

    return render(request, 'solicitar_servicio.html', {'form': form})




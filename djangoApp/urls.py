"""
URL configuration for djangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('servicios/', views.servicios, name='servicios'),
    path('logout/',views.signout, name='logout'),
    path('IniciarSesion/',views.IniciarSesion, name='IniciarSesion'),
    path('despliegueServidores/', views.despliegueServidores, name='despliegueServidores'),
    path('servicioWeb/',views.servicioWeb, name='servicioWeb'),
    path('implementacionIa/',views.implementacionIa, name='implementacionIa'),
    path('solicitar_servicio/', views.solicitar_servicio, name='solicitar_servicio')
]

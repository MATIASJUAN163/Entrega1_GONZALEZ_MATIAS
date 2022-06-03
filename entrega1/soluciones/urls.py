from django.urls import path
from . import views

urlpatterns = [
    path("" , views.inicio , name="" ),
    path("listaModem" , views.listaModem , name="listaModem" ),
    #path("altaModem" , views.altaModem ),
    path("listaMeter" , views.listaMeter , name="listaMeter" ),
    #path("altaMeter" , views.altaMeter ),
    path("listaWeb" , views.listaWeb , name="listaWeb" ),
    #path("altaWeb" , views.altaWeb),
    path("contacto" , views.contacto ),
    path("formularioModem" , views.formularioModem ),
    path("formularioMeter" , views.formularioMeter ),
    path("formularioWeb" , views.formularioWeb ),
    path("buscarModem" , views.buscarModem , name="BuscarModem" ),
    path("buscar" , views.buscar )
    
]
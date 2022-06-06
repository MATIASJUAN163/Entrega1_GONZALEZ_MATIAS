from django.urls import path
from . import views

urlpatterns = [

    path("" , views.inicio , name="inicio" ),
        
    path("listaModem" , views.listaModem , name="listaModem" ),
    path("listaMeter" , views.listaMeter , name="listaMeter" ),
    path("listaWeb" , views.listaWeb , name="listaWeb" ),
    
    path("formularioModem" , views.formularioModem ),
    path("formularioMeter" , views.formularioMeter ),
    path("formularioWeb" , views.formularioWeb ),
    path("buscarModem" , views.buscarModem , name="BuscarModem" ),
    
    path("buscar" , views.buscar )
    
]
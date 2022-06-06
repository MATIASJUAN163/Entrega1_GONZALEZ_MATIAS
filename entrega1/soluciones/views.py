from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from soluciones.models import Modem , Smartmeter , Webclient
from soluciones.forms import ModemFormulario , MeterFormulario , WebFormulario 


# Create your views here.

def inicio( request ) :

    return render( request , "index.html" )

def listaModem( request ) :

    modems = Modem.objects.all()
    datosModem = { "datosModem" : modems }

    return render( request , "listaModem.html" , datosModem )

def listaMeter( request ) :

    meters = Smartmeter.objects.all()
    datosMeter = { "datosMeter" : meters }

    return render( request , "listaMeter.html" , datosMeter )

def listaWeb( request ) :

    webs = Webclient.objects.all()
    datosWeb = { "datosWeb" : webs }

    return render( request , "listaWeb.html" , datosWeb )


def formularioModem( request ) :

    if request.method == "POST":

        modemFormulario = ModemFormulario( request.POST )

        if modemFormulario.is_valid():

            dicc = modemFormulario.cleaned_data

            modem = Modem( marca = dicc['marca'] , modelo = dicc['modelo'] , comunicacion = dicc['comunicacion'] , precio = dicc['precio'] )
            modem.save()
            return render( request , "formularioModem.html" )
    
    return render( request , "formularioModem.html")

def formularioMeter( request ) :

    if request.method == "POST":

        meterFormulario = MeterFormulario( request.POST )

        if meterFormulario.is_valid():

            dicc1 = meterFormulario.cleaned_data

            meter = Smartmeter( marca = dicc1['marca'] , modelo = dicc1['modelo'] , tipo = dicc1['tipo'] , precio = dicc1['precio'] )
            meter.save()
            return render( request , "formularioMeter.html")

    return render( request , "formularioMeter.html" )

def formularioWeb( request ) :

    if request.method == "POST":

        webFormulario = WebFormulario( request.POST )

        if webFormulario.is_valid():

            dicc2 = webFormulario.cleaned_data

            web = Webclient( marca = dicc2['marca'] , modelo = dicc2['modelo'] , precio = dicc2['precio'] )
            web.save()
            return render( request , "formularioWeb.html" )

    return render( request , "formularioWeb.html" )


def buscarModem( request ):

    return render( request , "buscarModem.html" )



def buscar( request ):

    if request.GET['marca']:

        marca = request.GET['marca']
       
        disp = Modem.objects.filter( marca__icontains = marca )

        return render( request , "resultadoBuscar.html" , { "modems" : disp ,"marca":marca } )

    else:
        return HttpResponse( "Campo vacío" )






        



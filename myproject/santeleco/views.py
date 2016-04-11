from django.shortcuts import render
from django.http import HttpResponse
from models import Actividad, Persona
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def actividades(request):
    if request.method =="POST":
        nombre = request.POST.get('nombre')
        horario = request.POST.get('horario')
        actividad = Actividad(nombre=nombre, horario=horario)
        actividad.save()

    respuesta= "ACTIVIDADES"
    apuntados = Actividad.objects.all()
    respuesta += '<ul>'
    for apuntado in apuntados:
        respuesta += '<li><a href="' + str(apuntado.id) + '">' + apuntado.nombre + '</a>'
    respuesta += "</ul>"

    context = {'contenido': respuesta}
    return render(request, 'actividades.html', {'context': context})

@csrf_exempt
def actividad(request, identificador):
    if request.method =="POST":
        nombre = request.POST.get('nombre')
        grado = request.POST['grado']
        actividad = Actividad.objects.get(id=identificador)
        persona = Persona(nombre=nombre, grado=grado, actividad=actividad)
        persona.save()

    try:
        actividad = Actividad.objects.get(id=identificador)
    except Actividad.DoesNotExist:
        return HttpResponse("No existe la actividad " + str(identificador))
    respuesta = "La actividad " + actividad.nombre + " tendra lugar el " +   str(actividad.horario)

    #los apuntados

    respuesta += "<br/></br>Apuntados: <ul>"
    apuntados = Persona.objects.filter(actividad=actividad)
    for apuntado in apuntados:
        respuesta += "<li>" + apuntado.nombre + " , " + apuntado.grado
    respuesta += "</ul>"

    if request.user.is_authenticated():
        loggeado = '<p>Logeado como ' + request.user.username
        loggeado += '<br><a href="/logout"><button>Logout</button></a>'
    else:
        loggeado = '<p>No estas logeado'
        loggeado += '<br><a href="/login"><button>Loggeate</button></a>'


    context = {'contenido': respuesta, 'loggeado': loggeado}
    return render(request, 'actividad.html', {'context': context})

def usuario(request):
    if request.user.is_authenticated():
        respuesta = 'Eres ' + request.user.username
    else:
        respuesta = 'Entra en tu cuenta o registrate <a href="/login"><button>Login</button></a>'
    return HttpResponse(respuesta)



# Create your views here.

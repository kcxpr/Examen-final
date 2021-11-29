from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CursoForm
from pelicula.models import Curso, Asignacion

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'])
            for alumno_id in request.POST.getlist('alumnos'):
                asignacion = Asignacion(alumno_id=alumno_id, curso_id = curso.id)
                asignacion.save()  
            messages.add_message(request, messages.SUCCESS, 'Curso creado exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
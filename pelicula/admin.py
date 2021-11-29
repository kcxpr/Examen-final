from django.contrib import admin

from pelicula.models import Alumno, AlumnoAdmin, Curso, CursoAdmin
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso,CursoAdmin)

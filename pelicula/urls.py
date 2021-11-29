from django.conf.urls import url
from django.conf.urls import url
from . import views


urlpatterns = [
    url('curso/nuevo/', views.pelicula_nueva, name='curso_nuevo'),
    ]
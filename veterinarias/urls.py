from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^veterinarias/nueva/$', views.veterinarias_nueva, name='veterinarias_nueva'),
    url(r'^veterinario/(?P<pk>[0-9]+)/$', views.veterinarias_nueva, name='veterinario_editar'),
    ]

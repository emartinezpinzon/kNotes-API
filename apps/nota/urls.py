from django.conf.urls import url
from apps.nota import views

urlpatterns = [
    url(r'^etiquetas/$', views.EtiquetaList.as_view()),
    url(r'^etiquetas/(?P<pk>[0-9]+)/$', views.EtiquetaDetail.as_view()),
    url(r'^notas/$', views.NotaList.as_view()),
    url(r'^notas/(?P<pk>[0-9]+)/$', views.NotaDetail.as_view()),
    url(r'^notas/etiqueta/(?P<pk>[0-9]+)/$', views.NotaEtiquetaList.as_view()),
]

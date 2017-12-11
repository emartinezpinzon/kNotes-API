from django.conf.urls import url
from apps.nota import views

urlpatterns = [
    url(r'^etiquetas/$', views.EtiquetaList.as_view()),
]

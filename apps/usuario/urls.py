from django.conf.urls import url
from apps.usuario import views

urlpatterns = [
    url(r'^registro/api/$', views.RegistroAutorList.as_view()),
    url(r'^login/api/$',views.LoginList.as_view()),
]

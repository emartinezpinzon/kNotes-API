from django.conf.urls import url
from apps.usuario import views

urlpatterns = [
    url(r'^registro/$', views.RegistroList.as_view()),
    url(r'^login/$',views.LoginList.as_view()),
]

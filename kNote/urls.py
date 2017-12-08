from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^nota/', include('apps.nota.urls', namespace='nota')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
]

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin

# dois imports importantes para que se possa fazer upload de imagens corretamente no django
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('simplemooc.core.urls', namespace="core")),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace="courses")),
    url(r'^admin/', include(admin.site.urls)),
)

# se estiver no ambiente de teste carrega os arquivos de media deste ambiente
# caso contrario deve carregar de um lugar especifico do servidor só para guardar
# estes arquivos

# melhor pratica ter no ambiente de desenvolvimento ter um servidor só para estes arquivos de imagens
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

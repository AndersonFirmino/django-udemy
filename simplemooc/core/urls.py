# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core.views', # este é o prefixo que as demais urls vão usuario
    # isto facilita a escrita e organiza mais o código
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contato'),
)

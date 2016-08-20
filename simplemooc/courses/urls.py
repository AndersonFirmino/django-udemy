# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views', # este é o prefixo que as demais urls vão usuario
    # isto facilita a escrita e organiza mais o código
    url(r'^$', 'index', name='index'),
)

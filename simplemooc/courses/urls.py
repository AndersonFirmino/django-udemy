# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views', # este é o prefixo que as demais urls vão usar
    # isto facilita a escrita e organiza mais o código
    url(r'^$', 'index', name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
)

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('', # este é o prefixo que as demais urls vão usuario

    url(r'^entrar/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^cadastre-se/$', 'simplemooc.accounts.views.register', name='register'),

)

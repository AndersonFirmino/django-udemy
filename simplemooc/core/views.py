# -*- coding: utf-8 -*- 
# django tem um atalho, para renderizar suas templates. Este atalho é o render
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("Ola!") # primeiro exemplo de formas de renderizar html
    return render(request, 'home.html', {'usuario': 'Anderson'})

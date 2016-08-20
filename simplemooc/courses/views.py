from django.shortcuts import render

from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all() # acessando o model (banco de dados) e trazendo os dados para view
    template_name = 'courses/index.html'

    context = {
        'courses': courses
    }

    return render(request, template_name, context)

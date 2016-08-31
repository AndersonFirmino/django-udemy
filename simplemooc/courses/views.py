# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse

# Create your views here.
def index(request):
    courses = Course.objects.all() # acessando o model (banco de dados) e trazendo os dados para view
    template_name = 'courses/index.html'

    context = {
        'courses': courses
    }

    return render(request, template_name, context)


# def details(request, pk):
#     # course = Course.objects.get(pk=pk)
#     course = get_object_or_404(Course, pk=pk)
#
#     context = {
#         'course': course
#     }
#     template_name = 'courses/details.html'
#
#     return render(request, template_name, context)

def details(request, slug):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        # print(request.POST)
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            print(form.cleaned_data) # esta é a maneira que usamos para acessar os dados.
            form = ContactCourse()


    else:
        form = ContactCourse()

    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'

    return render(request, template_name, context)

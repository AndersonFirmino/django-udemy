# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    """Esta classe representa as opções do admin"""

    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Course, CourseAdmin)
# com esta linha acima linkamos o models que criamos no arquivo models.py
# e passamos a classe models do curso.

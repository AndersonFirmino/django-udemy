from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    """Esta classe representa as opções do admin"""

    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin) # com esta linha linkamos o models que criamos no arquivo models.py e passamos a classe models do curso.

# -*- coding: utf-8 -*-
from django.db import models

# defindo um manager, personalizado para fazer as buscas.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
                models.Q(name__icontains=query) | models.Q(description__icontains=query)
            )


# Create your models here.
class Course(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho")
    # dizendo que este campo abaixo não é obrigatorio
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(
            upload_to='courses/images', verbose_name='Imagem',
            null=True, blank=True
        )

    create_at = models.DateTimeField('Criado em', auto_now_add=True)  # util para saber quando foi criado
    update_at = models.DateTimeField('Atualizado em', auto_now=True)  # util para saber quando foi atualizado

    objects = CourseManager()

    # isto é util para corrigir a apresentação deste models no django admin
    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug})

    class Meta:
        """Esta classe altera como os dados serão exibidos no django Admin"""

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

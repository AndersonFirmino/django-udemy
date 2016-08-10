# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Course(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho")
    # dizendo que este campo abaixo não é obrigatorio
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(
            upload_to='courses/images', verbose_name='Imagem',
            null=True, blank=True
        )

    create_at = models.DateTimeField('Criado em', auto_now_add=True)  # util para saber quando foi criado
    update_at = models.DateTimeField('Atualizado em', auto_now=True)  # util para saber quando foi atualizado

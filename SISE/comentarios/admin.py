# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields=['comentario']
    search_fields = ['comentario']
    list_filter = ['comentario']
    list_display =['comentario']
admin.site.register(models.Comentarios,PostAdmin)

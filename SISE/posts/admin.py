# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['message']
    search_fields = ['message']
    list_filter = ['message']
    list_display =['message']
admin.site.register(models.Post,PostAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cuentas.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'egreso', 'carrera', 'telefono', 'user_info')

    def user_info(self, obj):
        return obj.descripcion

    def get_queryset(self,request):
        queryset= super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset
admin.site.register(UserProfile, UserProfileAdmin)

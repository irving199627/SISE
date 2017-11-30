# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Comentarios(models.Model):
    post = models.ForeignKey(User, related_name="comentarios")
    created_at = models.DateTimeField(auto_now=True)
    comentario = models.TextField()
    comentario_html = models.TextField(editable = False)

    def __str__(self):
        return self.comentario

    def save(self,*args,**kwargs):
        self.comentario_html = misaka.html(self.comentario)
        super(Comentarios, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'comentarios:single',
            kwargs={
                'username': self.user.username,
                'pk':self.pk
            }
        )
    class Meta:
        ordering = ["-created_at"]
        unique_together = ['post', 'comentario']

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable = False)
    imagen = models.ImageField(upload_to='profile_image2',blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super(Post, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse(
            'posts:single',
            kwargs={
                'username': self.user.username,
                'pk':self.pk
            }
        )
    class Meta:
        ordering = ["-created_at"]
        unique_together = ['user','message']

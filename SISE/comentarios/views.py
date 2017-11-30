# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic
from django.views.generic import (UpdateView)

from braces.views import SelectRelatedMixin

from . import forms
from . import models
from posts.forms import PostForm

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class ComentarioList(SelectRelatedMixin,generic.ListView):
    model = models.Comentarios
    select_related = ("user",)

class UserComentario(generic.ListView):
    model = models.Comentarios
    template_name = "comentario/user_comentario_lis.html"

    def get_queryset(self):
        try:
            self.comentario_user = User.objects.prefetch_related("post").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.comentario_user.comentarios.all()

    def get_context_data(self,**kwargs):
        context = super(UserComentario, self).get_context_data(**kwargs)
        context["comentario_user"] = self.comentario_user
        return context

class ComentarioDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Comentarios
    select_related = ("user",)

    def get_queryset(self):
        queryset = super(ComentarioDetail, self).get_queryset()
        return queryset.filter(
            user_username__iexact=self.kwargs.get("username")
        )

class CreateComentario(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('comentario',)
    model = models.Comentarios

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CreateComentario, self).form_valid(form)

class DeleteComentario(LoginRequiredMixin, SelectRelatedMixin,generic.DeleteView):
    model = models.Comentarios
    select_related=("user",)
    success_url = reverse_lazy('comentarios:all')

    def get_queryset(self):
        queryset = super(DeleteComentario, self).get_queryset()
        return queryset.filter(user_id=self.request.post.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,"Comentario Eliminado")
        return super(DeletePost, self).delete(*args,**kwargs)

class UpdateComentario(LoginRequiredMixin,SelectRelatedMixin,generic.UpdateView):
    model = models.Comentarios
    select_related = ("user",)
    fields = ['comentario']
    success_url = reverse_lazy('comentarios:all')

    def get_queryset(self):
        queryset = super(UpdateComentario, self).get_queryset()
        return queryset.filter(user_id=self.request.post.id)

    def update(self,*args,**kwargs):
        messages.success(self.request, "Comentario Actualizado")
        return super(UpdateComentario, self).update(*args,**kwargs)

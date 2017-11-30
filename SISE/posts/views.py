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
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user",)

class UserPosts(generic.ListView):
    model = models.Post
    template_name = "post/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ("user",)

    def get_queryset(self):
        queryset = super(PostDetail, self).get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message',)
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False) # guarda los datos sin almacenar en  la base
        self.object.user = self.request.user
        self.object.save() # guarda en la base
        return super(CreatePost, self).form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ("user",)
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super(DeletePost, self).get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request, "Post Eliminado")
        return super(DeletePost, self).delete(*args,**kwargs)


class UpdatePost(LoginRequiredMixin,SelectRelatedMixin,generic.UpdateView):
    model = models.Post
    select_related = ('user',)
    fields=['message',]
    template_name = 'posts/post_form2.html'
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super(UpdatePost,self).get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def update(self,*args,**kwargs):
        messages.success(self.request, "Post Actualizado")
        return super(UpdatePost, self).update(*args,**kwargs)

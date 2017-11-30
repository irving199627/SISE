# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.views.generic  import CreateView,TemplateView, UpdateView, DetailView,DeleteView
from braces.views import SelectRelatedMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from . import forms
from . import models


# Create your views here.
class Registro(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'cuentas/registrar.html'


class UsuariosView(TemplateView):
    template_name = 'cuentas/usuarios.html'
    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        args = {'users':users}
        return render(request, self.template_name, args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'cuentas/perfil3_pasteles.html',args)

def edit_profile(request):
    if request.method=='POST':
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid:
            form.save()
            return redirect('cuentas:perfil')
    else:
        form= forms.EditProfileForm(instance=request.user.userprofile)
        args={ 'form':form }
        return render(request,'cuentas/userprofile_form.html', args)

def delete_usuario(request, pk, template_name='cuentas/user_confirm_delete.html'):
    usuario = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('cuentas:lista_usuarios')
    return render(request, template_name, {'usuario':usuario})

def cambiar_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('cuentas:perfil')
        else:
            return redirect('cuentas:cambiar_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args={ 'form':form }
        return render(request,'cuentas/cambiar_password.html', args)

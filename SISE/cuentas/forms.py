#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from cuentas.models import UserProfile
from django import forms

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name', 'last_name','username', 'email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].label = 'Nombre(s)'
        self.fields['last_name'].label = 'Apellido(s)'
        self.fields['username'].label='Nombre de usuario'
        self.fields['email'].label = 'Correo'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label= 'Confirmar Contraseña'



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=(
        'carrera',
        'egreso',
        'telefono',
        'descripcion',
        'experiencia',
        'image',
        )
    def __init__(self, *args, **kwargs):
            super(EditProfileForm, self).__init__(*args,**kwargs)
            self.fields['image'].label = 'Imagen de Perfil'
# <li><a href="{% url 'cuentas:edit_profile' pk=user.userprofile.pk%}" class="waves-effect black-text"><i class="material-icons left">edit</i>Editar Perfil</a></li>

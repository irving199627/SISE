# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()


class UserProfile(models.Model): # Hereda de la clase model
    CARRERA = (
        ('Ingenieria En Sistemas','ISC'),
        ('Ingenieria Quimica','Ingenieria Quimica'),
        ('Ingenieria Bioquimica','Ingenieria Bioquimica'),
        ('Ingenieria Industrial','Ingenieria Industrial'),
        ('Ingenieria Electrica','Ingenieria Electrica'),
        ('Ingenieria Electronica','Ingenieria Electronica'),
        ('Ingenieria Mecanica','Ingenieria Mecanica'),
        ('Ingenieria Biomedica','Ingenieria Biomedica'),
        ('LAE','LAE'),
    )

    EGRESO = (
        ('1970','1970'),('1971','1971'),('1972','1972'),('1973','1973'),('1974','1974'),('1975','1975'),('1976','1976'),('1977','1977'),('1978',('1978')),('1979','1979'),
        ('1980','1980'),('1981','1981'),('1982','1982'),('1983','1983'),('1984','1984'),('1985','1985'),('1986','1986'),('1987','1987'),('1988',('1988')),('1989','1989'),
        ('1990','1990'),('1991','1991'),('1992','1992'),('1993','1993'),('1994','1994'),('1995','1995'),('1996','1996'),('1997','1997'),('1998',('1998')),('1999','1999'),
        ('2000','2000'),('2001','2001'),('2002','2002'),('2003','2003'),('2004','2004'),('2005','2005'),('2006','2006'),('2007','2007'),('2008',('2008')),('2009','2009'),
        ('2010','2010'),('2011','2011'),('2012','2012'),('2013','2013'),('2014','2014'),('2015','2015'),('2016','2016'),('2017','2017'),
    )
    user = models.OneToOneField(User)
    carrera = models.CharField(max_length=30, choices=CARRERA)
    egreso = models.CharField(max_length=4,choices=EGRESO)
    telefono = models.IntegerField(default=0)
    descripcion = models.TextField()
    experiencia = models.TextField()
    image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username


# crea un perfil de usuario junto al usuario creado
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

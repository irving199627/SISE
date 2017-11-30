from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import (
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
)

app_name= 'cuentas'

urlpatterns=[
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='cuentas/login2.html'), name ='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name = 'logout'),
    url(r'^registro/$',views.Registro.as_view(),name='registro'),
    url(r'^list/$',views.UsuariosView.as_view(),name='lista_usuarios'),
    url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),
    url(r'^profile/$',views.view_profile, name='perfil'),
    url(r'^profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_pk'),
    url(r'^delete/usuario/(?P<pk>\d+)/$',views.delete_usuario,name='delete_user'),
    url(r'^cambiar-password/$', views.cambiar_password, name= 'cambiar_password'),

    url(r'^password_reset/$', PasswordResetView.as_view(template_name='cuentas/reset_password.html',
        email_template_name='cuentas/reset_password_email.html',
        success_url='/cuentas/password_reset/done'), name='reset_password'),

    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='cuentas/reset_password_done.html'),
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='cuentas/reset_password_confirm.html',
         success_url='/cuentas/password_reset/complete'),
        name='password_reset_confirm'),

    url (r'^password_reset/complete/$',PasswordResetCompleteView.as_view(template_name='cuentas/reset_password_complete.html'),
     name='password_reset_complete'),

]

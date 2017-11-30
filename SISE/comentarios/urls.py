from django.conf.urls import url
from . import views

app_name = 'comentarios'

urlpatterns=[
    url(r"^$", views.ComentarioList.as_view(), name="all"),
    url(r"nuevo/$", views.CreateComentario.as_view(), name="create"),
    url(r"por/(?P<username>[-\w]+)/$",views.UserComentario.as_view(),name="for_user"),
    url(r"por/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.ComentarioDetail.as_view(),name="single"),
    url(r"eliminar/(?P<pk>\d+)/$",views.DeleteComentario.as_view(),name="delete"),
    url(r"update(?P<pk>\d+)/$",views.UpdateComentario.as_view(),name="update"),



]

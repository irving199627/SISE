from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns=[
    url(r"^$", views.PostList.as_view(), name="all"),
    url(r"nuevo/$", views.CreatePost.as_view(), name="create"),
    url(r"por/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"por/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    url(r"eliminar/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    url(r"update(?P<pk>\d+)/$",views.UpdatePost.as_view(),name="update"),



]

from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.post_list), # an empty string will match
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail), # post detail
	url(r'^post/new/$', views.post_new, name='post_new'), # new post
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'), # edit post
]
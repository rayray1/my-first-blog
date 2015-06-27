from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.post_list), # an empty string will match
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail), # post detail
	url(r'^post/new/$', views.post_new, name='post_new'), # new post
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'), # edit post
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'), # drafts
	url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'), # publish
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'), # remove

]

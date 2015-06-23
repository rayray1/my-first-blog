from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list), # an empty string will match
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
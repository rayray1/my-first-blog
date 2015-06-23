from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list), # an empty string will match
]
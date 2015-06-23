from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')), # import urls from blog app
]










# REGEX EXAMPLE - ^post/(\d+)/$
# ^post - tells django to take anything that has post/ at the beginning of the url(after ^)
# (\d+) - there will be a no.(one or more) & we want the no. captured & extracted
# / - tells django that another / character should follow
# $ - indicates the end of the url - meaning only strings ending with the / will match this pattern

# ^ - for beginning of text
# + - to indicate that the previous item shud be repeated at least once
# () - to capture a part of the pattern
# \d - for a digit
# $ - for end of text
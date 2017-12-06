from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/about$', 'salaries2017.views.About'),
    (r'^/search$', 'salaries2017.views.Search'),
    (r'^/(?P<id>[a-zA-Z0-9_.-]+)/(?P<name_slug>[a-zA-Z0-9_.-]+)$', 'salaries2017.views.PersonPage'),
    (r'^/(?P<company>[a-zA-Z0-9_.-]+)$', 'salaries2017.views.AgencyPage'),
    (r'^', 'salaries2017.views.Main'),
)

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^$', '{{ app_name }}.views.main', name = 'main'),

)
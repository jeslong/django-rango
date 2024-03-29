from django.conf.urls import patterns, url
from rango import views
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), 
	)

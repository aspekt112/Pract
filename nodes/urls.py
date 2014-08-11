from django.conf.urls import patterns, include, url
from nodes import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
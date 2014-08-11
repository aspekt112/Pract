from django.conf.urls import patterns, include, url
from django.contrib import admin
from nodes import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pract.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add-form/', views.add_form),
    url(r'^add/', views.add),
    url(r'^choose_db/', views.choose_db),
    url(r'^nodes/', include('nodes.urls')),
    #url(r'^table/', views.table),
    url(r'^admin/', include(admin.site.urls)),
)
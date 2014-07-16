from django.conf.urls import patterns, include, url
from pyfriend.views import register,login,logout
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),                     
    url(r'^$',include('pyfriend.urls')),
    url(r'^register/$',register),
    url(r'^login/$',login),
    url(r'^logout/$',logout),

 
)

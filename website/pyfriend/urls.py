from django.conf.urls import patterns, url
from pyfriend import views

 
urlpatterns = patterns('pyfriend.views',
    url(r'^$', 'home'),
    url(r'^register/$', 'register'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),


)

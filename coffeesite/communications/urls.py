from django.conf.urls import patterns, include, url
from communications import views

urlpatterns = patterns('',
    url(r'^contact_us/$', views.contact_us, name='contact_us'), # NEW MAPPING!
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^djangosite/', include('djangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
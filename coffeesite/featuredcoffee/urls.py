from django.conf.urls import patterns, include, url
from featuredcoffee import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    #url(r'^coffee/',views.coffee, name="coffee"),
    url(r'^coffee/(?P<year>\w+)/(?P<month>\w+)/$',views.coffee, name="coffee"),
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^djangosite/', include('djangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^', include('communications.urls')),
    url(r'^', include('faqs.urls')),
    url(r'^', include('featuredcoffee.urls')),
    url(r'^', include('memberships.urls')),
    # Examples:
    # url(r'^$', 'coffeesite.views.home', name='home'),
    # url(r'^coffeesite/', include('coffeesite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

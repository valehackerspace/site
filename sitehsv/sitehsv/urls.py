from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sistema.views.home', name='home'),
    url(r'^', include('sistema.urls')),
    #url(r'^sitehsv/', include('sitehsv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'sistema/login.html'}, name='login'),
    url(r'^logout/$', logout, {"next_page": "/"}, name='logout'),
)

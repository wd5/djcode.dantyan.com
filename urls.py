from django.conf.urls.defaults import *
#from views import hello, current_datetime, hours_ahead
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'djcode.views.welcome'),
    (r'^blog/', include('djcode.blog.urls')),
    
    # Example:
    # (r'^djcode/', include('djcode.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
) 

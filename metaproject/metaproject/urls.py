from django.conf.urls import patterns, include, url
from meta_list.views import view_meta
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metaproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^metaview/', view_meta, name = 'meta-view'),
    url(r'^admin/', include(admin.site.urls)),
)




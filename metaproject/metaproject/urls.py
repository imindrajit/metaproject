from django.conf.urls import patterns, include, url
from meta_list.views import view_meta, view_json
#from tastypie.api import Api
#from meta_list.api.resources import MyModelResource
from django.contrib import admin
admin.autodiscover()

'''v1_api = Api(api_name='v1')
v1_api.register(MyModelResource()) '''

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metaproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^api/', include(v1_api.urls)),
    url(r'^metaview/json/',view_json, name = 'json-view'),
    url(r'^metaview/$', view_meta, name = 'meta-view'),
    url(r'^admin/', include(admin.site.urls)),
)




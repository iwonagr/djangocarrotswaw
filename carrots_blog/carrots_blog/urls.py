from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrots_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'post.views.hello', name='hello'),
    url(r'^posty/$', 'post.views.list', name='lista'),
    url(r'^posty/(?P<id>\d)/$', 'post.views.show', name='pokaz'),
)

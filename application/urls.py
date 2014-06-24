from django.conf.urls import patterns, include, url
from django.contrib import admin

from application.settings import config as settings
from application.modules.web import views as web_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webAppSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    )

urlpatterns += patterns('',
    url(r'^js/environment\.js$', web_views.EnvironmentJS.as_view()),
    url(r'^$', web_views.DemoPage.as_view()),
)
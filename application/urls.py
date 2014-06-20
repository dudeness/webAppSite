from django.conf.urls import patterns, include, url

from django.contrib import admin

from application.modules.web import views as web_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webAppSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', web_views.DemoPage.as_view())
)

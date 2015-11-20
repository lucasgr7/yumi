from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_service.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^exercito/', include('jogo.urls_exercito')),
    url(r'^tatic/', include('jogo.urls_tatic')),
    url(r'^soldado/', include('jogo.urls_soldado')),
    url(r'^personage/', include('vocabulary.urls')),
)

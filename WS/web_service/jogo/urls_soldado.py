from django.conf.urls import include, url, patterns

urlpatterns = patterns('jogo.views',
    url(r'^inserir/$', 'inserir_soldado', name='inserir_soldado'),
    url(r'^list/$', 'list_soldado', name='list_soldado'),
    url(r'^delete/(?P<codigo>\d+)/$', 'delete_soldado', name='delete_soldado'),
)

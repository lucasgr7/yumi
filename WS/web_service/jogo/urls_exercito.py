from django.conf.urls import include, url, patterns

urlpatterns = patterns('jogo.views',
    url(r'^inserir/$', 'inserir_exercito', name='inserir_exercito'),
    url(r'^list/$', 'list_exercito', name='listar_exercito'),
    url(r'^delete/(?P<codigo>\d+)/$', 'delete_exercito', name='delete_exercito'),
)

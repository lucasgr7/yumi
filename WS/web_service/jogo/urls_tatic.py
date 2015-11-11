from django.conf.urls import include, url, patterns

urlpatterns = patterns('jogo.views',
    url(r'^inserir/$', 'inserir_tatic', name='inserir_tatic'),
    # url(r'^list/$', 'list_tatic', name='listar_exercito'),
    # url(r'^delete/(?P<codigo>\d+)/$', 'delete', name='delete_usuario'),
)

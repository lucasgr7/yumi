from django.conf.urls import include, url, patterns

urlpatterns = patterns('usuario.views',
    url(r'^inserir/$', 'inserir', name='inserir_usuario'),
    url(r'^list/$', 'list', name='listar_usuario'),
    url(r'^delete/(?P<codigo>\d+)/$', 'delete', name='delete_usuario'),
)

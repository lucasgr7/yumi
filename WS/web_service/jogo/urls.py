from django.conf.urls import include, url, patterns

urlpatterns = patterns('jogo.views',
    url(r'^inserirExercito/$', 'inserir', name='inserir_usuario'),
    url(r'^list/$', 'list', name='listar_usuario'),
    url(r'^delete/(?P<codigo>\d+)/$', 'delete', name='delete_usuario'),
)

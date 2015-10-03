from django.conf.urls import include, url, patterns

urlpatterns = patterns('usuario.views',
    url(r'^inserir/$', 'inserir', name='inserir_usuario'),
)

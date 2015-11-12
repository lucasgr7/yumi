from django.conf.urls import include, url, patterns

urlpatterns = patterns('vocabulary.views',
    url(r'^new_personage/$', 'new_personage_name', name='new_personage_name'),
    # url(r'^list/$', 'list', name='listar_usuario'),
    # url(r'^delete/(?P<codigo>\d+)/$', 'delete', name='delete_usuario'),
)

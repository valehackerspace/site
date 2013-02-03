from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^eventos/$', 'sistema.views.eventos_list', name='eventos-list'),
    url(r'^projetos/$', 'sistema.views.projeto_list', name='projeto-list'),

    url(r'^post/(?P<pk>\d+)/$', 'sistema.views.post', name='post'),
    url(r'^evento/(?P<pk>\d+)/$', 'sistema.views.evento', name='evento'),
    url(r'^projeto/(?P<pk>\d+)/$', 'sistema.views.projeto', name='projeto'),
)

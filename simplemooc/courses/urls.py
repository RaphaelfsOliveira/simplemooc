from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', views.undo_enrollment, name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<id>\d+)/$', views.show_announcement, name='show_announcement'),
    url(r'^(?P<slug>[\w_-]+)/aulas/$', views.lessons, name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aula/(?P<id>\d+)/$', views.lesson, name='lesson'),
    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<id>\d+)/$', views.material, name='material'),
    #url(r'^(?P<pk>\d+)/$', views.details, name='details'),
]

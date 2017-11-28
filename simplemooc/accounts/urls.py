from django.conf.urls import include, url
from django.contrib.auth import views as django_views
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', django_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', django_views.logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastrar/$', views.register, name='register'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^senha/$', views.edit_password, name='password'),
    url(r'^resetar-password/$', views.password_reset, name='password_reset'),
    url(r'^confirmar-resetar-password/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
]

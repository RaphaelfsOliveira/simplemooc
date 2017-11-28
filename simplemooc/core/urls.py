from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
]

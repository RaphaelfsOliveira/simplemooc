from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.band, name='band'),
    url(r'^bands/$', views.band_listing, name='bands'),
    url(r'^bands/(?P<pk>\d+)/$', views.band_detail, name='band_detail'),
    url(r'^bandform/$', views.BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', views.MemberForm.as_view(), name='member_form'),
    url(r'^contact/$', views.band_contact, name='contact'),
    url(r'^protected/$', views.protected_view, name='protected'),
    url(r'^accounts/login/$', views.message),
]

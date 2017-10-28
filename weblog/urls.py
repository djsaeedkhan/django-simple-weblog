from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'add$', views.add, name='add'),
    url(r'list$', views.list, name='list'),

    url(r'detail/(?P<id>[0-9]{1})/$', views.detail,name='detail'),
    url(r'detail/(?P<id>[0-9]{2})/$', views.detail,name='detail'),
    url(r'detail/(?P<id>[0-9]{3})/$', views.detail,name='detail'),

    url(r'update/(?P<id>[0-9]{1})/$', views.update,name='update'),
    url(r'update/(?P<id>[0-9]{2})/$', views.update,name='update'),
    url(r'$', views.index, name='index'),
]
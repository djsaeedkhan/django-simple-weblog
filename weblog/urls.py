from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'add$', views.add, name='add'),
    url(r'list$', views.list, name='list'),
    url(r'detail/(?P<id>[0-9])$', views.detail,name='detail'),
    url(r'$', views.index, name='index'),
]
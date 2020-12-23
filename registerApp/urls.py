
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newuser/$', views.newuser),
    url(r'^listuser/$', views.listuser),
    url(r'^api/tutorials$', views.register_user),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.register_detail),
    url(r'^api/tutorials/published$', views.register_list),
]


from django.conf.urls import url

from . import views
from . import views_django_modelform

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newuser/$', views.newuser),
    url(r'^newuser_modelform/$', views_django_modelform.django_form),
    url(r'^listuser/$', views.listuser),
    #url(r'^login/(?P<email>)$', views.loginuser),
    #url(r'^api/tutorials$', views.register_user),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.register_detail),
    #url(r'^api/tutorials/published$', views.register_list),
]

from django.conf.urls import url

from . import views
from . import views_django_modelform
from . import views_usercreationform

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newuser/$', views.newuser),
    url(r'^newuser_modelform/$', views_django_modelform.django_form),
    url(r'^newuser_usercreationform/$', views_usercreationform.signup_view),
    url(r'^listuser/$', views.listuser),

    url(r'^sent/$', views_usercreationform.activation_sent_view, name="activation_sent"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views_usercreationform.activate, name="activate"),
    #url(r'^login/(?P<email>)$', views.loginuser),
    #url(r'^api/tutorials$', views.register_user),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.register_detail),
    #url(r'^api/tutorials/published$', views.register_list),
]

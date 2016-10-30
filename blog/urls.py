from django.conf.urls import url
from . import views
urlpatterns = [ url(r'^$', views.post_list, name='post_list'), 
url(r'^about$', views.post_list_about, name='post_list_about'), 
url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^categories/(?P<cat>[\w\-]+)/$', views.categories, name='categories')
    
    
]
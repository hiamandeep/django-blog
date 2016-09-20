from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_feed, name='post_feed'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	# url(r'^test$',views.test1,name='test'),
	url(r'^post/new$',views.post_new,name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^tag/(?P<tage>[\w\-]+)/$', views.tag_filter, name='tag_filter'), #the regex patten should be valid

]
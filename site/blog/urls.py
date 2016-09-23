from django.conf.urls import include, url 
from . import views


urlpatterns = [
	
	# post views
	url(r'^$', views.post_home, name = 'post_home' ), 
    url(r'^all/$', views.post_list, name = 'post_list'),
	url(r'^(?P<post>[-\w]+)/$', views.post_detail, name = 'post_detail'),
    url(r'^(?P<post>[-\w]+)/share/$', views.post_share, name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),

]




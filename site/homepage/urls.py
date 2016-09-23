from django.conf.urls import include, url 
from . import views

urlpatterns = [
	
    url(r'^$', views.show_homepage, name='homepage'),
    url(r'^blog', include('blog.urls',
							namespace = 'blog',
							app_name = 'blog')),
]
    

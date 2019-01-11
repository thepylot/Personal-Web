from django.conf.urls import include, url

from post.views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Examples:
    # url(r'^$', 'spiders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 
    url(r'^blog/', blog, name='blog'),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail" ),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete" ),
    url(r'^(?P<id>\d+)/update/$', post_update, name="update" ),

    #dashboard urls
    url(r'^admin/', admin, name='admin'),
    url(r'^create/', post_create, name='create'),

    #category urls
    url(r'^software/', cat_software, name='software'),
    url(r'^mobile/', cat_mobile, name='mobile'),
    url(r'^game/', cat_game, name='game'),
    url(r'^space/', cat_space, name='space'),
    url(r'^socialmedia/', cat_socialmedia, name='socialmedia'),
    url(r'^science/', cat_space, name='science'),
    url(r'^equipment/', cat_equipment, name='equipment'),
        

   
    
  
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
